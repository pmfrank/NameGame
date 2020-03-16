# dict_factory function found at: https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
# Originally posted by Alex Martelli on Stack Overflow
# Function is used to covert sqlite3 queary results into a list of dictionaries

import os
import pygame as pg
from gtts import gTTS
import sqlite3
import time

def display(caption, size, fill, fullscreen=False):

    pg.init()
    pg.display.set_caption(caption)
    if fullscreen:
        screen = pg.display.set_mode(size, pg.FULLSCREEN)
    else:
        screen = pg.display.set_mode(size)
    screen.fill(fill)
    pg.display.flip()
    return screen

def change_bgcolor(surface, fill):

    surface.fill(fill)
    pg.display.flip()
    return surface

def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_database(db, table, columns):


    #Set up query string to unpack columns tuple
    q = 'SELECT '
    for x, column in enumerate(columns):
        q = q + '{},'
    q = q[:-1]
    q = q + ' FROM {}'.format(table)
    q = q.format(*columns)


    # Execute the sql query and return the resultsc
    with sqlite3.connect(db) as conn:
        conn.row_factory = _dict_factory
        c = conn.cursor()
        c.execute(q)
        return c.fetchall()

def show_img(screen, img, x, y):

    img_rect = img.get_rect()
    img_rect.centerx = x
    img_rect.centery = y
    screen.blit(img, img_rect)
    return img

def speak(text, screen):

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