import streamlit as st
import segno
import io


@st.dialog("Share Subject")
def share_subject_dialog(subject_name, subject_code):

    app_domain = "quickattend.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Share Subject Link and QR Code")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Share Join Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info(
            "Share the above join code or URL with your students so they can easily join the subject using the Student Portal."
        )

    with col2:
        st.markdown("### QR Code")
        st.image(
            out.getvalue(),
            caption="Students can scan this QR code to join the subject directly.",
        )
