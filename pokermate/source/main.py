# Imports
import os
from PIL import Image
import numpy as np
import streamlit as st
import requests
import time


###################################################
# CONFIG
###################################################

## Backend endpoints
API_URL         =       "http://127.0.0.1:5000/"

## Metadata
__author__      =       "pranjal"
__version__     =       "1.0.0"

## Streamlit specifics ::
st.set_page_config(layout="wide", page_title="PokerMate", page_icon="❄:spades:")


###################################################
# UTILS
###################################################
def display_sidebar():
    st.sidebar.write("")
    st.sidebar.title("Poker Hand Detector")
    st.sidebar.markdown("---")
    st.sidebar.header("How to Use:")
    st.sidebar.markdown(
        "1. Upload an image of a poker hand.\n"
        "2. Click the 'Detect Poker Hand' button to analyze the image.\n"
        "3. Results will be displayed in the main area."
    )

    st.sidebar.write("")
    st.sidebar.write(""" <h3>File Format Supported:</h3>
                        <span class="tags">.jpg</span> 
                        <span class="tags">.jpeg</span> 
                        <span class="tags">.png</span>""", unsafe_allow_html=True)
    #api_auth()
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.markdown("---")
    st.sidebar.write("""
        Built by © Pranjal

        #### Github: https://github.com/pranzell
        #### Website: https://pranzell.github.io/
        """)
    return

def display_header():
    st.markdown(
        """
            <div/>
            <style>
                div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
                    position: sticky;
                    top: 2.875rem;
                    background-color: white;
                    z-index: 999;
                }
            </style>
        """,
        unsafe_allow_html=True
    )

###################################################
# MAIN
###################################################
def main():

    ## Sidebar
    display_sidebar()

    ## Header
    with st.container():
        st.title(":spades:  PokerMate  :spades:")
        st.subheader("Your smart poker assistant")
        #st.image("./public/img/logo.png", width=200, )
        display_header()

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:

        # Display uploaded image
        st.image(uploaded_file, caption="Your Image", width=600)

        # Button to trigger the detection
        if st.button("Detect Poker Hand"):

            with st.spinner("Running neural networks..."):
                time.sleep(2)

                # # Send image to Flask API for detection
                files = {"file": uploaded_file}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    result = response.json()

                    # Display detected labels
                    st.subheader("Detected Cards:")
                    st.write(result["labels"])

                    # Display best hand rank
                    st.subheader("Best Poker Hand Possible for you")
                    st.write(result["best_hand_rank"])
                    st.session_state.uploaded = True

                    st.sidebar.write(" ")
                    st.sidebar.write(" ")
                    st.sidebar.write(" ")

                    # Display original and annotated images
                    col1, col2 = st.columns(2)
                    with col1:
                       st.subheader("Original Image")
                       st.image(result["image_path"], width=400)
                    with col2:
                       st.subheader("Detected Image")
                       st.image("./uploads/detected.jpg", width=400)
                else:
                    st.error("Error processing the image. Please try again.")

############################################################################################################
if __name__ == "__main__":
    main()
