# Speech to text program
import speech_recognition as speech
import pyttsx3

import os
import openai
from dotenv import load_dotenv

OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY

# TEXT TO SPEECH
def SpeakText(command):
    
    # init engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
# speech recognizer
recognizer = speech.Recognizer()

def record_text():
    while True:
        try:
            # use the microphone as an input source
            with speech.Microphone() as source:
                
                # prepare the recognizer for input
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                print("I'm listening")
                
                #listen for the input
                audio = recognizer.listen(source)
                
                #use google for recognizing
                Text = recognizer.recognize_whisper(audio)
                return Text
            
        except speech.RequestError as e:
            print("Could not request results; {0}".format(e))
        except speech.UnknownValueError:
            print("Unknown error occured")
            
def send_to_gpt(messages, model="gpt-4o"):
    
        
    


messages = []

while True:
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_gpt(messages)
    SpeakText(response)

    print(response)
