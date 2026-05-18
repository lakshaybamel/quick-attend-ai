import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
import pandas as pd
from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write(
        "In this dialog, you can record classroom audio to automatically identify which enrolled students are present based on their voice profiles. Please ensure that the students have registered their voice embeddings for accurate identification."
    )

    audio_data = None

    audio_data = st.audio_input("Record classroom audio here")

    if st.button("Analyze Audio", width="stretch", type="primary"):
        with st.spinner("Processing audio and identifying speakers..."):
            enrolled_res = (
                supabase.table("subject_students")
                .select("*, students(*)")
                .eq("subject_id", selected_subject_id)
                .execute()
            )
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning("No students are currently enrolled in this subject.")
                return
            candidates_dict = {
                s["students"]["student_id"]: s["students"]["voice_embedding"]
                for s in enrolled_students
                if s["students"].get("voice_embedding")
            }

            if not candidates_dict:
                st.error(
                    "No enrolled students have registered voice embeddings. Unable to perform voice attendance."
                )
                return

            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node["students"]
                score = detected_scores.get(student["student_id"], 0.0)
                is_present = bool(score > 0)

                results.append(
                    {
                        "Name": student["name"],
                        "ID": student["student_id"],
                        "Source": score if is_present else "-",
                        "Status": "✅ Present" if is_present else "❌ Absent",
                    }
                )

                attendance_to_log.append(
                    {
                        "student_id": student["student_id"],
                        "subject_id": selected_subject_id,
                        "timestamp": current_timestamp,
                        "is_present": bool(is_present),
                    }
                )
            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log,
            )

    if st.session_state.get("voice_attendance_results"):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)