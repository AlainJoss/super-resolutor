import streamlit as st
import resolutor
import cv2

if 'original' not in st.session_state:
    st.session_state.original = None

if 'upscaled' not in st.session_state:
    st.session_state.upscaled = None

if 'succeded' not in st.session_state:
    st.session_state.succeded = None

st.title("Super-Resolutor")
st.write("Super resolutor is a super-hero which enables you to x4 the resolution of your images.")
st.write("### Upload Image")

uploaded_file = st.file_uploader(label="Upload your image", type=['png', 'jpg'])

if uploaded_file is not None:

    opencv_image = resolutor.file_to_opencv_image(uploaded_file)
    st.session_state.original = opencv_image

    with st.form("upscale", clear_on_submit=True):
        if st.form_submit_button("Upscale"):
            with st.spinner("Upscaling in progress ..."):
                try:
                    upscaled = resolutor.upscale(opencv_image)
                    st.session_state.upscaled = upscaled
                    st.session_state.succeded = True

                    st.write("### Comparison")

                    col1, col2 = st.columns(2)

                    with col1: 
                        st.write("Original image")
                        st.image(st.session_state.original)
                    with col2:
                        st.write("Upscaled image")
                        st.image(st.session_state.upscaled)

                except:
                    st.write("An error has occured. It may be that the image has a too high resolution already.")

    if st.session_state.succeded:
        # Convert numpy array to binary data
        upscaled_rgb = cv2.cvtColor(st.session_state.upscaled, cv2.COLOR_BGR2RGB)
        _, buffer = cv2.imencode('.png', upscaled_rgb)
        binary_data = buffer.tobytes()

        st.write("### Download")

        st.download_button(
            label='Upscaled Image',
            file_name='upscaled.png',
            data=binary_data
        )