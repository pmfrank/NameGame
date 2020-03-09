import os
import pygame as pg
from gtts import gTTS

def speak(text):

    """
    This function will handle all the spoken lines for the interface
    """

    tts = gTTS(text=text, lang='en-us')

    filename = 'voice.mp3'
    tts.save(filename)

    pg.mixer.init()
    pg.mixer.music.load(filename)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy() == True:
        continue

    os.remove(filename)