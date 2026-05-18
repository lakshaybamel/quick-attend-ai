import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write(
        "To create a new subject, please fill in the details below. The subject code should be unique and will be used by students to enroll in this subject. Make sure to provide a clear and descriptive name for the subject, as well as the section information if applicable. Once you click 'Create Subject Now', the subject will be created and you can start sharing the join code with your students."
    )
    sub_id = st.text_input("Subject Code", placeholder="Eg: CS101", max_chars=20)
    sub_name = st.text_input(
        "Subject Name", placeholder="Eg: Introduction to Computer Science"
    )
    sub_section = st.text_input("Section", placeholder="Eg: A")

    if st.button("Create Subject", type="primary", width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject created successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error creating subject: {str(e)}")
        else:
            st.warning("Please fill in all the fields to create a subject.")
