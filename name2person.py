"""  
This game will allow the player to pick wich person goes with the name given
"""

import sqlite3
import pygame as pg
from variable import color
from pyautogui import size
from speech import speak
from display import display
from random import randrange, choice

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


pg.init()

bgcolor = color['white']
screen = display("Name To Person", size(), bgcolor)

width = size()[0]
height = size()[1]
clock = pg.time.Clock()

with sqlite3.connect('family.db') as conn:
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute('select rowid, name, gender, relation, image from family_info')
    data = c.fetchall()


image1 = pg.image.load('img/amy.JPG')
image2 = pg.image.load('img/daniel.JPG')
image3 = pg.image.load('img/braydon.JPG')

def showimg(img, x, y):

    img_rect = img.get_rect()
    img_rect.centerx = x
    img_rect.centery = y
    screen.blit(img, img_rect)

picked = list()
person = list()

photo1 = False
photo2 = False
photo3 = False
selected = False

while True:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            if image1.get_rect().collidepoint(x, y):
                speak('That is the correct answer!')
                picked = []
                person = []
                photo1 = False
                photo2 = False
                photo3 = False
                selected = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()
    screen.fill(bgcolor)

    while not photo1:
        rowid = randrange(5)+1
        while rowid in picked:
            rowid = randrange(5) + 1
        picked.append(rowid)
        for entry in data:
            if entry['rowid'] == rowid:
                person.append(entry)
                image1 = pg.image.load(f'img/{person[0]["image"]}')
                img_w, img_h = image1.get_size()
                image1 = pg.transform.scale(image1,(int(img_w*.25),int(img_h*.25)))
        photo1 = True
    while not photo2:
        rowid = randrange(5)+1
        while rowid in picked:
            rowid = randrange(5) + 1
        picked.append(rowid)
        for entry in data:
            if entry['rowid'] == rowid:
                person.append(entry)
                image2 = pg.image.load(f'img/{person[1]["image"]}')
                img_w, img_h = image2.get_size()
                image2 = pg.transform.scale(image2,(int(img_w*.25),int(img_h*.25)))
        photo2 = True
    while not photo3:
        rowid = randrange(5)+1
        while rowid in picked:
            rowid = randrange(5) + 1
        picked.append(rowid)
        for entry in data:
            if entry['rowid'] == rowid:
                person.append(entry)
                image3 = pg.image.load(f'img/{person[2]["image"]}')
                img_w, img_h = image3.get_size()
                image3 = pg.transform.scale(image3,(int(img_w*.25),int(img_h*.25)))
        photo3 = True
    showimg(image1, width // 4, height // 4)
    showimg(image2, width // 2, height // 4)
    showimg(image3, (3*width) // 4, height // 4)

    while not selected:
        ans = randrange(3)
        answer = person[ans]
        print(answer)
        selected = True

    pg.display.flip()
    pg.display.update()

    clock.tick(30)
