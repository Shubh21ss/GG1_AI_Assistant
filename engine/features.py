import pygame.mixer
import pygame.time
import eel


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

