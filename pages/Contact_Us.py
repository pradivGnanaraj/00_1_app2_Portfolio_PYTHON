import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv("topics.csv")

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")

    option = st.selectbox(
        "Select a Subject",
        df["Topic:"]
    )
    raw_message = st.text_area("Your message here")
    message = f"""\
Subject: New email from {user_email}

From : {user_email}
{raw_message} 
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")


