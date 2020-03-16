from variable import color, name_var_dict
from helper_functions import get_database, speak, display, show_img
from random import shuffle, choice
import pygame as pg
from pyautogui import size
from classes import Button

pg.init()

bgcolor = color['white']
screen = display("Relationship To Person", size(), bgcolor)

width, height = size()
clock = pg.time.Clock()

data = get_database('family.db','family_info',('rowid','name','gender','relation','image'))

relations = ['aunt','uncle','cousin','grandma','grandpa','sister','mom','dad']

lastans = 'Filler'

while True:
    correct = False
    spoken = False
    shuffle(data)

    person = data[0]
    while person['relation'] == lastans:
        shuffle(data)
        person = data[0]

    image =  pg.image.load(f'img/{person["image"]}')
    ans = person['relation']

    guesses = [person['relation']]
    for i in range(2):
        select = choice(relations)
        while select in guesses:
            select = choice(relations)
        guesses.append(select)

    shuffle(guesses)

    height_div = [4,2,1.3]

    font = pg.font.SysFont('quicksandmedium', 80)

    while not correct:

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if locals()[ans].is_over(pos):
                    speak('That is the correct answer')
                    correct = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    exit()
        screen.fill(bgcolor)
        font = pg.font.SysFont('quicksandmedium', 60)
        text = font.render(f'This is {person["name"].capitalize()}. {"He" if person["gender"]=="boy" else "She"} is your... ', 1, color['black'])
        
        screen.blit(text, (width//10,height//10))

        show_img(screen, image, width//4, height//2)
        for x, guess in enumerate(guesses):
            locals()[guess] = Button(color['magenta'],(width//1.3),(height//height_div[x]),300,75, text=guess)
            locals()[guess].draw(screen)
        pg.display.flip()
        while not spoken:
            speak(f'This is {person["name"].capitalize()}. {"He" if person["gender"]=="boy" else "She"} is your... ')
            spoken = True
        lastans = ans