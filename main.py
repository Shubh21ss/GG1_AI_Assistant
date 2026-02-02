import os
import eel
from engin.features import *
eel.init('www')

playAssistSound()
os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode='chrome', host='localhost', block=True)