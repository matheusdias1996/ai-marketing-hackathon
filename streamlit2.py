import streamlit as st

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

button_clicked = st.button("OK")
