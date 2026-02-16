import streamlit as st

st.title("Smart Illegal Bowling Detection & Feedback Generator")

st.write("This is a demo version of the project.")

uploaded_video = st.file_uploader("Upload Bowling Video", type=["mp4", "avi"])

if uploaded_video:
    st.video(uploaded_video)
    st.success("Video uploaded successfully!")
