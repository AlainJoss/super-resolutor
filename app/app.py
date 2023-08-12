import streamlit as st
import resolutor
import os
import cv2
import numpy as np

st.title("Super-Resolutor")

st.write("Super resolutor is a super-hero which enables you to x4 the resolution of your images.")

os.makedirs("image", exist_ok=True)

st.write("### Upload Image")

uploaded_file = st.file_uploader(label="Upload your image", type=['png', 'jpg'])

if uploaded_file is not None:
    with st.spinner("Upscaling in progress ..."):
        # Convert the file to an opencv image.
        try:
            opencv_image = resolutor.file_to_opencv_image(uploaded_file)

            upscaled = resolutor.upscale(opencv_image)

            st.write("### Comparison")

            col1, col2 = st.columns(2)

            with col1: 
                st.write("Original image")
                st.image(opencv_image)
            with col2:
                st.write("Upscaled image")
                st.image(upscaled)

            # Convert numpy array to binary data
            _, buffer = cv2.imencode('.png', upscaled)
            binary_data = buffer.tobytes()

            st.write("### Download")

            st.download_button(
                label='Upscaled Image',
                file_name='upscaled.png',
                data=binary_data
            )
        except:
            st.write("An error has occured. It may be that the image has a too high resolution already.")