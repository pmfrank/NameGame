# from speech import speak
from speech import speak
from display import display, change_bgcolor
from pyautogui import size
from variable import color
from textbox import TextBox as tb
import pygame as pg

# I'm makeing a chage to the code. I'll show what changes then I'll send it to GitHub, the I'll explain my commands
#This will be the new commit. I meant git checkout -b branch. not git -chechout -b branch

bgcolor = color['white']
screen = display('Family Name Game', size(), bgcolor)

textBox = tb()
shiftDown = False
textBox.rect.center = [320,240]


clock = pg.time.Clock()

while True:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()
        if event.type == pg.KEYUP:
            if event.key in [pg.K_RSHIFT, pg.K_LSHIFT]:
                shiftDown = False
        if event.type == pg.KEYDOWN:
            textBox.add_chr(pg.key.name(event.key), shiftDown)
            if event.key == pg.K_SPACE:
                textBox.text += " "
                textBox.update()
            if event.key in [pg.K_RSHIFT, pg.K_LSHIFT]:
                shiftDown = True
            if event.key == pg.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if event.key == pg.K_RETURN:
                if len(textBox.text) > 0:
                    speak(textBox.text)
                    textBox.text = None
                    textBox.update()
    screen.fill(bgcolor)
    screen.blit(textBox.image, textBox.rect)
    pg.display.flip()
    pg.display.update()

    clock.tick(30)

        