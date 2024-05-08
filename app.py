import streamlit as st
import cv2 as cv
from backend import detect

st.title("Motion Detection")
run = st.checkbox('Run')
camera = cv.VideoCapture(0)

FRAME_WINDOW = st.image([])
while run:
    _, frame = camera.read()
    finframe=detect(frame)
    FRAME_WINDOW.image(finframe)
else:
    st.write(":red[Turned Off]")
