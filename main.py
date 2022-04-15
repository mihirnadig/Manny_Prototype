# Hopefully I rmbr how python works
import streamlit as st
from PIL import Image

print("test")
print("did this work")

image = Image.open('MannyRepresentation.jpg')
audio_file_3a = open('adultcase3a.mp3', 'rb')
audio_file_4a = open('adultCase4a.mp3', 'rb')

audio_bytes_3a = audio_file_3a.read()
audio_bytes_4a = audio_file_4a.read()

st.title('Auscultation Prototype')
st.markdown("This prototype represents the feedback received when using Manny the Modular Mannequin. The picture "
            "below represents the user placing the stethoscope. If \"Placed\" on any of the four positions, "
            "press the corresponding button below to represent the audio feedback the user would recieve.")
st.image(image, caption='Mannequin Representation')

st.subheader("Audio Feedback Representation")

# 4a is aortic valve
if st.button('Orange Placement'):
    st.write('Aortic Valve')
    st.audio(audio_bytes_4a, format='audio/ogg')

# 3a is mitral valve
if st.button('Pink Placement'):
    st.write('Mitral Valve')
    st.audio(audio_bytes_3a, format='audio/ogg')

st.title('Under Construction')
if st.button('Blue Placement'):
    st.write('Pulmonary Valve')

if st.button('Yellow Placement'):
    st.write('Tricuspid Valve')
