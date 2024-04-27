from openai import OpenAI
import streamlit as st

openai_api_key = "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"
st.set_page_config(page_title="AB+ Testing Platform",
                   page_icon="🚀", layout="wide")
st.title("💬 AB+")
st.caption("🚀 Faster iterations for your AB testing!")

# Image upload section
uploaded_file = st.file_uploader(
    "What ad would you like to optimize?", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    # To See details
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)
    # To Display image
    st.image(uploaded_file, caption='Uploaded Image.')
