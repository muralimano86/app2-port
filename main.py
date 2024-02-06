import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Muralidaran Manoharan")
    content = """I am Oracle PLSQL developer learning Python. 
    I have 16 years of experience in PLSQL, Business Objects"""
    st.info(content)

content2 = """
Below are some of the apps I built in Python. Feel free to contact me!
"""
st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.title(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.title(row["title"])