import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Muralidaran Manoharan")
    content="""I am Oracle PLSQL developer learning Python. 
    I have 16 years of experience in PLSQL, Business Objects"""
    st.info(content)


st.write("Below are some of the apps I built in Python. Feel free to contact me!")