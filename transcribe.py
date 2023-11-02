# import openai
import speech_recognition as sr


# OpenAI API key

# Text-to-speech engine
import whisper


def listen_and_respond(model="large"):
    """
    Listen for audio input, recognize it and respond using OpenAI
    """
    # Create speech recognizer object
    r = sr.Recognizer()

    # Listen for input
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=10)

    # Recognize input
    try:
        print("Recognizing...")
        prompt = r.recognize_google(audio, language="sv-SE", show_all=False)
        #prompt = r.recognize_whisper(audio, language="swedish", model=model) # https://github.com/Uberi/speech_recognition/blob/8b07762f80dfec2d34fb4c40b8eddbb7ec503521/speech_recognition/__init__.py#L1460
    except sr.UnknownValueError:
        print("Could not understand audio")
        prompt = "12345"

    print("You asked:", prompt)
    return prompt


if __name__ == "__main__":
    while True:
        listen_and_respond()


