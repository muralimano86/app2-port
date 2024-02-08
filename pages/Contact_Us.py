import streamlit as st
from send_mail import send_mail


st.header("Contact Me")

with st.form(key="email_form"):
    email_address = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New mail from {email_address}

From: {email_address}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Your mail was sent successfully")