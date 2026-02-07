import pyttsx3
import speech_recognition as sr
import eel

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayText("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking before a phrase is considered complete
        r.adjust_for_ambient_noise(source) # adjust for ambient noise
        audio = r.listen(source, timeout=10, phrase_time_limit=6) # 10 seconds to wait for a phrase, 6 seconds max phrase length

    try:
        print("Recognizing...")
        eel.DisplayText("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        # speak_text(f"You said: {query}")
        eel.DisplayText(query)
        eel.ShowHood()


    except Exception as e:
        return ""
    
    return query.lower()

# text = take_command()

# speak_text(text)

# speak_text("Hello, how can I assist you today?")
@eel.expose
def allCMDs():
    query = take_command()
    print(f"Received command: {query}")

    if 'open' in query:
        # print("Opening application...")
        from engine.features import openApp
        openApp(query)
    else:
        print("Command not recognized.")
