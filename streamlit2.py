import streamlit as st
from streamlit_chat import message

# user_input = st.text_input("Enter a description of the demographic you are looking to target. For example, \"the advertisement targets consumers of a supermarket in Vitória, Espírito Santo, Brazil. The supermarket targets people who value convenience and fresh products in general, but also just people who are looking to make grocery purchases. The supermarket is also famous for being related to local products and supporting the community. It also has a good assortment of Arabic products given owners are Lebanese descendants\"", "hi")

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
button_clicked = st.button("OK")

print("SELECTED: ", selected)
print("SELECTED: ", type(selected))