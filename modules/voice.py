import pyttsx3
import os

def generate_voice(incoming_text):
    text = incoming_text.split("_")[1]
    engine = pyttsx3.init(driverName='sapi5')
    engine.save_to_file(text, 'tmp.mp3')
    engine.runAndWait()
    return os.getcwd() + '\\tmp.mp3'