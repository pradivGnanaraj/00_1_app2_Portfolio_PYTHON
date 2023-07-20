import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=400)

with col2:
    st.title("Pradiv Gnanaraj")
    content = """
    Hi, I am Pradiv! I am a Python programmer, Cloud Devops and MLOps. 
    """
    st.info(content)

