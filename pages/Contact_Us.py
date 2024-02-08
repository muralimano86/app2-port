import streamlit as st


st.header("Contact Me")

with st.form(key="email_form"):
    email_address = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        print(button)
        print("I am pressed!")