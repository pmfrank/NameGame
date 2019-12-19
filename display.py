import pygame as pg
import time

def display(caption, size, fill):

    pg.init()
    pg.display.set_caption(caption)
    screen = pg.display.set_mode(size, pg.FULLSCREEN)
    screen.fill(fill)
    pg.display.flip()

    return screen

def change_bgcolor(surface, fill):

    surface.fill(fill)

    pg.display.flip()

    return surface