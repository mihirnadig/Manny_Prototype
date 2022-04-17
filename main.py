# Hopefully I rmbr how python works
import streamlit as st
from PIL import Image

question_answer = False

image = Image.open('MannyRepresentation.jpg')
audio_file_3a = open('adultcase3a.mp3', 'rb')
audio_file_4a = open('adultCase4a.mp3', 'rb')

audio_bytes_3a = audio_file_3a.read()
audio_bytes_4a = audio_file_4a.read()

st.title('Auscultation Prototype')
st.subheader("ME 533 - EPE Group 8")
st.subheader("Mihir Nadig, Meryl Suresh, Nicholas Robinson, Chris Jurkiewics")
st.markdown("This prototype represents the feedback received when using Manny the Modular Mannequin. The picture "
            "below represents the user placing the stethoscope. To \"Placed\" on any of the four positions, "
            "press the corresponding button below to represent the audio feedback the user would recieve.")
st.image(image, caption='Mannequin Representation')

st.subheader("Audio Feedback Representation")

if st.button("Reset/Wrong Placement"):
    print("Random Placement")
    st.write("...")

# 4a is aortic valve
if st.button('Orange Placement'):
    st.write('Aortic Valve')
    st.audio(audio_bytes_4a, format='audio/ogg')

# 3a is mitral valve
if st.button('Pink Placement'):
    st.write('Mitral Valve')
    st.audio(audio_bytes_3a, format='audio/ogg')

st.title('Companion App - Analytics Prototype')
col1, col2, col3, = st.columns(3)
with col1:
    st.metric(label="Percentage Correct", value="70 %", delta="5 %")
with col2:
    st.metric(label="Elapsed Time", value="12 m", delta="-1 m")
with col3:
    st.metric(label="Accuracy", value="90 %", delta="7 %")

st.title('Below Elements Are Still Under Construction')
if st.button('Blue Placement'):
    st.write('Pulmonary Valve')

if st.button('Yellow Placement'):
    st.write('Tricuspid Valve')
    st.write("What is the correct Diagnosis?")
    col1, col2, col3, = st.columns(3)
    with col1:
        if st.button("This is still a test 1"):
            question_answer = True
    with col2:
        st.checkbox("This is still a test2")
    with col3:
        st.checkbox("This is still a test3")
st.subheader("Last Diagnosis was:")

if question_answer == True:
    st.succes("you got one right num nuts")
else:
    st.error("Still wrong")
