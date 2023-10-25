# import openai
import speech_recognition as sr


# OpenAI API key

# Text-to-speech engine
# import whisper


def listen_and_respond():
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

    # Try to recognize the audio

    # model = whisper.load_model("tiny")

    # transcription = model.transcribe(
    #        str(audio_path), language="Swedish", initial_prompt=initial_prompt
    #    )
    try:
        prompt = r.recognize_google(audio, language="sv-SE", show_all=False)
    # prompt = r.recognize_whisper(audio, language="swedish")
    except sr.UnknownValueError:
        print("Could not understand audio")
        prompt = ""

    print("You asked:", prompt)
    return prompt


if __name__ == "__main__":
    while True:
        listen_and_respond()
