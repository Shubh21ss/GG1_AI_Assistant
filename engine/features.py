import os
import pygame.mixer
import pygame.time
import eel

from engine.cmd import speak_text
from engine.config import Assistant_Name


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