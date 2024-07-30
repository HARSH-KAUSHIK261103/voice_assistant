import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("hey, good morning ")
    elif  hour>12 and hour<=18:
        speak("hey, good afternoon")
    else:
        speak("hey,good evening")

    speak("Please tell me how can i help you")
