from gtts import gTTS
#from playsound import playsound
#import pyttsx3
from pydub import AudioSegment
from pydub.playback import play


def text_to_speech(phrase):
    tts = gTTS(text=phrase, lang="sv", slow=True)
    tts.save("phrase.mp3")
    sound = AudioSegment.from_mp3("phrase.mp3")
    sound = sound.speedup(1.4)
    play(sound)

    #playsound("phrase.mp3")



def text_to_speech2(phrase):
    # Initialize the converter
    converter = pyttsx3.init("dummy")

    # Set properties before adding
    # Things to say

    # Sets speed percent
    # Can be more than 100
    converter.setProperty("rate", 150)
    # Set volume 0-1
    converter.setProperty("volume", 0.7)

    # Queue the entered text
    # There will be a pause between
    # each one like a pause in
    # a sentence
    converter.say(phrase)

    # Empties the say() queue
    # Program will not continue
    # until all speech is done talking
    converter.runAndWait()


if __name__ == "__main__":
    text_to_speech("Hej! Viktor, jag är din robot-kompis!")
