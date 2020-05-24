import relationships2person
import name2person
import nameguess
import draw_game
from classes import Button
from variable import color
from helper_functions import speak, display
import pygame as pg
from pyautogui import size

pg.init()

bgcolor = color['black']
screen = display("Mahala's Games", size(), bgcolor, fullscreen=True)

width, height = size()
clock = pg.time.Clock()

n2p_button = Button(color['green'],25, 100, 400, 75, text='Name 2 Person')
r2p_button = Button(color['yellow'],25, 200, 450, 75, text='Relationship 2 Person')
ng_button = Button(color['blue'],25, 300, 400, 75, text='Name Guessing')
draw_button = Button(color['magenta'],25, 400, 400, 75, text='Drawing Fun')
quit_button = Button(color['red'],(width - 300),(height - 150), 200, 75, text='Quit')

playing = True

def draw():
    screen.fill(bgcolor)
    n2p_button.draw(screen)
    r2p_button.draw(screen)
    ng_button.draw(screen)
    draw_button.draw(screen)
    quit_button.draw(screen)
    pg.display.flip()

while playing:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_g:
                playing = False
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if n2p_button.is_over(pos):
                name2person.main()
            if r2p_button.is_over(pos):
                relationships2person.main()
            if ng_button.is_over(pos):
                nameguess.main()
            if draw_button.is_over(pos):
                draw_game.main()
            if quit_button.is_over(pos):
                playing = False
    draw()