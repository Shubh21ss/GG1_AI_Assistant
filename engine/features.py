import os
import re
import pygame.mixer
import pygame.time
import eel

from engine.cmd import speak_text
from engine.config import Assistant_Name
import pywhatkit as kit


#sound function for assistant startup sound
def playAssistSound():
    music_file =   "www\\assets\\audio\\start_sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

# sound function for assistant startup sound
@eel.expose
def playClickSound():
    music_file =   "www\\assets\\audio\\click_sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)


def openApp(query):
    query = query.replace(Assistant_Name, "")
    query = query.replace("open", "")
    query.lower()

    #for opening applications based on voice command for future use
    # if 'chrome' in query:
    #     os.system('start chrome.exe')
    # elif 'notepad' in query:
    #     os.system('start notepad.exe')
    # elif 'calculator' in query:
    #     os.system('start calc.exe')
    # else:
    #     print("Application not recognized.")
    
    if query != "":
        speak_text(f"Opening {query}")
        os.system(f'start {query}.exe')

    else:
        speak_text(f"{query} is not recognized. Please try again.")


def PlayYT(query):
    search_query = extractYTSearchQuery(query)
    if search_query:
        speak_text(f"Playing {search_query} on YouTube")
        # os.system(f'start https://www.youtube.com/results?search_query={search_query}')
        kit.playonyt(search_query)
    else:
        speak_text("Sorry, I couldn't extract the search query. Please try again.")


def extractYTSearchQuery(query):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, query, re.IGNORECASE)
    return match.group(1) if match else None