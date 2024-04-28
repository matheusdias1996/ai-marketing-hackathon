import streamlit as st
import subprocess
import json

# user_input = st.text_input("Enter a description of the demographic you are looking to target. For example, \"the advertisement targets consumers of a supermarket in Vitória, Espírito Santo, Brazil. The supermarket targets people who value convenience and fresh products in general, but also just people who are looking to make grocery purchases. The supermarket is also famous for being related to local products and supporting the community. It also has a good assortment of Arabic products given owners are Lebanese descendants\"", "hi")

st.set_page_config(page_title="AB+ Testing Platform",
                   page_icon="🚀", layout="wide")
st.title("💬 AB+")
st.caption("🚀 Faster iterations for your AB testing!")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

#icon("search")
selected = st.text_input("Enter a description of the demographic you are looking to target.")
original_post_text = st.text_area("Add information that should be in the post",
                                  placeholder="Type here any specific information that must be included in the advertisement post.")

# Image upload section
uploaded_file = st.file_uploader(
    "What ad would you like to optimize?", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    # To See details
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    # st.write(file_details)
    # To Display image
    st.image(uploaded_file, caption='Uploaded Image.')

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

button_clicked = st.button("OK")
if button_clicked and uploaded_file is not None:
    command = f'python generate_ad.py --image_path "{uploaded_file.name}" --demographic "{selected}" --original_post_text "{original_post_text}" --image_url1 "{uploaded_file.name}" --post_text1 "{original_post_text}" --image_url2 "{uploaded_file.name}" --post_text2 "{original_post_text}"'
    subprocess.run(command, shell=True)

    # Read the output data
    with open('output_data.json', 'r') as json_file:
        results = json.load(json_file)
    # Initialize or update session state
    if 'index' not in st.session_state:
        st.session_state.index = 0
    max_index = len(results) - 1

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 10, 1])
    with col1:
        if st.button("←"):
            if st.session_state.index > 0:
                st.session_state.index -= 1
    with col3:
        if st.button("→"):
            if st.session_state.index < max_index:
                st.session_state.index += 1

    # Display current image and text
    result = results[st.session_state.index]
    st.image(result['image_filename'], caption='Generated Image')
    st.write(f"{result['post_text']}")

    st.markdown("---")  # Separator


# TODO: Make it interactive so button does something when you click
