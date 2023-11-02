
# import openai
import speech_recognition as sr
import argparse
import os
# OpenAI API key

# Text-to-speech engine
import whisper


def listen_and_respond(model="large", output_folder="."):
    """
    Listen for audio input, recognize it and respond using OpenAI
    """
    # Create speech recognizer object
    r = sr.Recognizer()

    # Listen for input
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Save audio
    print("saving...")
    if output_folder != ".":
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    #with open(f"{output_folder}/audio.wav", "wb") as f:
    #    f.write(audio.get_wav_data())


    #audio.export("audio.mp3", format="mp3")


    # Recognize input
    try:
        print("Recognizing...")
        prompt = r.recognize_google(audio, language="sv-SE", show_all=False)
        #prompt = r.recognize_whisper(audio, language="swedish", model=model) # https://github.com/Uberi/speech_recognition/blob/8b07762f80dfec2d34fb4c40b8eddbb7ec503521/speech_recognition/__init__.py#L1460
    except sr.UnknownValueError:
        print("Could not understand audio")
        prompt = ""

    print("You said:", prompt)
    with open(f"{output_folder}/prompt.txt", "a") as f:
        f.write(prompt)
        f.write("\n")
        

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--model', type=str, default="large", help='model to use')
    parser.add_argument('--output_folder', type=str, default=".", help='output folder')
    
    args = parser.parse_args()

    model = args.model
    output_folder = args.output_folder

    while True:
        listen_and_respond(model, output_folder)

