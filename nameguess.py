from variable import color
from helper_functions import get_database, speak, display, show_img
import pygame as pg
from pyautogui import size
from classes import Button
from random import shuffle
import speech_recognition as sr

def main():
    pg.init()

    bgcolor = color['white']
    screen = display("Guess the Name", size(), bgcolor, fullscreen=True)

    width, height = size()
    clock = pg.time.Clock()

    data = get_database('family.db','family_info',('rowid','name','gender','relation','image'))

    lastans = None
    playing = True

    while playing:
        
        correct = False
        spoken = False

        shuffle(data)
        person = data[0]
        while person['name'] == lastans:
            shuffle(data)
            person = data[0]

        image = pg.image.load(f'img/{person["image"]}')
        ans = person['name']
        
        font = pg.font.SysFont('quicksandmedium', 80)

        while not correct and playing:

            screen.fill(bgcolor)
            text = font.render(f'This is your {person["relation"]}. {"His" if person["gender"]=="boy" else "Her"} name is... ', 1, color['black'])
            screen.blit(text, (width//10,height//10))
            show_img(screen, image, width//4, height//2)
            pg.display.flip()
            while not spoken:
                speak(f'This is your {person["relation"]}. {"His" if person["gender"]=="boy" else "Her"} name is... ')
                spoken = True
            lastans = ans

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)

            if r.recognize_google(audio) == 'exit':
                playing = False
            
            if r.recognize_google(audio).lower() == person['name']:
                speak("That is correct")
                correct = True
            elif r.recognize_google(audio) == 'retry':
                correct = True
            elif not r.recognize_google(audio) == 'exit':
                speak("Sorry, try again")
            


if __name__ == "__main__":
    main()