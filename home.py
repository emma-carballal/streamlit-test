import streamlit as st

app_title = "Streamlit Test"
st.set_page_config(page_title=app_title, page_icon="🚀", layout="wide")
st.title("Test streamlit website")
st.write("---")

a = st.text_area("Describe what you'd like to hear")

button = st.button('Get me some songs')

if button:
    st.write("Give me a second, I'll get you some bangers!")
