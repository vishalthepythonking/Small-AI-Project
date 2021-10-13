import sys
import webbrowser
from datetime import datetime
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("...........")
        return "none"
    query = query.lower()
    return query


# to wish
def wish():
    now = datetime.now()
    hours = int(now.strftime("%H"))
    minn = now.strftime("%M")
    sec = now.strftime("%S")

    if hours >= 0 and hours < 12:
        speak("good morning sir")
    elif hours > 12 and hours < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak('The running time is:-')
    if 0 <= hours < 12:
        speak(f" {hours}:{minn} A M")
    elif 12 <= hours < 24:
        speak(f" {hours}:{minn} P M")

    speak("Hello sir i am Alice, your personal study companiyan")
    speak("Please tell me what can i do for you sir")
    speak("I am Listening")




def TaskExecution():
    wish()
    while True:
        # if 1:

        query = takecommand().lower()
        # logic building for tasks
        if "wake up" in query:
            speak("I am up sir")

        elif "open youtube" in query:
            speak("Ok i am open youtube")
            webbrowser.open("www.youtube.com")


        elif "play songs on youtube" in query:

            speak("Ok sir , I  am playing  the  song on youtube")

            speak("I hope do you like this song sir")

            kit.playonyt("memorise")

        elif "thank you" in query:
            speak("thank you for using me sir, good day sir")
            sys.exit()

        speak("sir,do you have any other work")






if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()

        elif 'goodbye' in permission:
            speak("thanks for using me sir, have a good day")
            sys.exit()

