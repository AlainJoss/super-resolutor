from cv2 import dnn_superres
import models
import cv2
import numpy as np
import streamlit as st

def file_to_opencv_image(uploaded_file):
    try:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # Convert from BGR to RGB
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        
        return opencv_image
    except Exception as e:
        st.error(f"Error converting uploaded file: {e}")
        return None


def upscale(img):
    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read the desired model
    sr.readModel(models.X4_MODEL)

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel("edsr", 4)

    # Upscale the image
    result = sr.upsample(img)

    # Save the image
    return result