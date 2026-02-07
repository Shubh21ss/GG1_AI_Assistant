import os
import re
from sqlite3 import Cursor
import sqlite3
import webbrowser
import pygame.mixer
import pygame.time
import eel

from engine.cmd import speak_text
from engine.config import Assistant_Name
import pywhatkit as kit


conn = sqlite3.connect('GG1.db')
cursor = conn.cursor()

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
    query = query.replace("open", "").strip().lower()
    
    if query != "":
        try:
            # first check the sys_cmds table for a matching application name
            cursor.execute("SELECT path FROM sys_cmds WHERE LOWER(name)=?", (query,))
            result = cursor.fetchall()

            if len(result) != 0:
                speak_text(f"Opening {query}")
                os.startfile(result[0][0])
                return
            
            # if the application is not found in the sys_cmds table, check the web_cmds table for a matching URL
            cursor.execute("SELECT url FROM web_cmds WHERE LOWER(name)=?", (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak_text(f"Opening {query}")
                webbrowser.open(results[0][0]) # why i am using results[0][0] because fetchall() returns a list of tuples, and we need to access the first tuple and then the first element of that tuple to get the URL
                return
            
            speak_text("Opening {query}")
            try:
                os.system(f'start {query}.exe')
            except Exception as e:
                speak_text(f"Unable to open {query}. Error: {str(e)}")

        except Exception as e:
            speak_text(f"Something went wrong: {str(e)}")


    #for opening applications based on voice command for future use
    # if 'chrome' in query:
    #     os.system('start chrome.exe')
    # elif 'notepad' in query:
    #     os.system('start notepad.exe')
    # elif 'calculator' in query:
    #     os.system('start calc.exe')
    # else:
    #     print("Application not recognized.")
    
    # if query != "":
    #     speak_text(f"Opening {query}")
    #     os.system(f'start {query}.exe')

    # else:
    #     speak_text(f"{query} is not recognized. Please try again.")


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