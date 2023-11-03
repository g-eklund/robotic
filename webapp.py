import streamlit as st
import speech_recognition as sr
import os
from gpt import gpt

# Function to recognize speech
def recognize_speech(language, output_folder):
    recognizer = sr.Recognizer()

    
    if not os.path.exists(output_folder) and output_folder is not None:
        os.makedirs(output_folder)

    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        st.write("Recognizing...")
        if language == 'Swedish':
            text = recognizer.recognize_google(audio, language='sv-SE', show_all=False)
        else:
            text = recognizer.recognize_google(audio)
        st.write(text)
        #st.write(text)
        with open(f"{output_folder}/prompt.txt", "a") as f:
            f.write(text)
            f.write("\n")

    except sr.UnknownValueError:
        st.write("")
    except sr.RequestError:
        st.write("Sorry, I could not request results. Please check your internet connection.")

# Streamlit App
# Add modular logo
st.markdown('<div style="position: absolute; top: 10px; right: 10px;"><img src="https://i0.wp.com/conference.gaia.fish/wp-content/uploads/2022/02/Modulai-logo-1-e1645287158279.png" alt="Logo" style="width:300px;height:90px;"></div>', unsafe_allow_html=True)

st.title("Transcribe")
language = st.selectbox("Select Language", ["English", "Swedish"])
folder  = st.text_input("Enter Folder Name", None)
stop = st.button("Stop")


if st.button("Record Audio"):
    st.write(f"Please speak in {language}")
    while True:
        recognize_speech(language, folder)
        if stop:
            st.write("Stopped.")
            break

if st.button("Summarize"):
    if language == "Swedish":
        preprompt = "kan du sammanfatta följande text för mig så detaljerat och strukturerat som möjligt? \n"
    else:
        preprompt = "can you summarize the following text for me as detailed and structured as possible? \n"
    with open(f"{folder}/prompt.txt", "r") as f:
        
        prompt = f.read()
    st.write("Summarizing this text: ")
    st.write(prompt)
    prompt = preprompt + prompt
    
    try:   
        response = gpt([dict(role="user", content=prompt)])
        st.write(response)
    except Exception as e:
        st.write("Sorry, I could not request results. Please check your internet connection or your API key")
        st.write(e)



            

