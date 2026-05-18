import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    # Render header and apply styling
    header_home()
    style_background_home()
    style_base_layout()

    # Create two-column layout for Student and Teacher portals
    col1, col2 = st.columns(2, gap="large")

    # Student Portal Section
    with col1:
        st.header("I'm Student")
        st.image("https://i.ibb.co/wF8G10rq/Student.png", width=120)
        if st.button(
            "Student Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    # Teacher Portal Section
    with col2:
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/9HnVRZzH/teacher.png", width=120)
        if st.button(
            "Teacher Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()
