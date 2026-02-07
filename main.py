import os
import eel
from engine.features import *
from engine.cmd import *
from engine.config import Assistant_Name
eel.init('www')

playAssistSound()
os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode='chrome', host='localhost', block=True)