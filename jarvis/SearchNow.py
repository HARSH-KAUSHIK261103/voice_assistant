import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"you said:{query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()



def SearchGoogle(query):
    # if "google" in query:
        # import wikipedia as googleScrap
        # query = query.replace("jarvis","")
        # query = query.replace("google search ","")
        # query = query.replace("google","")
        speak("this is what i found on google")
        # try:
        #     pywhatkit.search(query)
        #     result = googleScrap.summary(query,1)
        #     speak(result)
        # except:
        #     speak("no speakable output available")

def SearchYoutube(query):
    if "youtube" in query:
        speak("this is what i found on youtube")
        query = query.replace("jarvis","")
        query = query.replace("youtube search ","")
        query = query.replace("youtube ","")
        web="https://www.youtube.com/results?search_query="+ query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done")


