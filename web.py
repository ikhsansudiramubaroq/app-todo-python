import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("Aplikasi Todo")
st.subheader("Ini adalah aplikasi ToDo saya")
st.write("Aplikasi ini membuat anda menjadi semakin produktif")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Masukkan todo baru")