import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time
from src.database.db import create_attendance


def show_attendance_result(df, logs):
    st.write("Please review the attendance results below. If everything looks correct, click 'Confirm & Save' to save the attendance records. If you need to make changes, click 'Discard' to go back and retake attendance.")
    st.dataframe(df, hide_index=True, width="stretch")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Discard", width="stretch"):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button("Confirm & Save", width="stretch", type="primary"):
            try:
                create_attendance(logs)
                st.toast("Attendance records saved successfully!")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error("Error saving attendance records: " + str(e))


@st.dialog("Attendance Results")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)
