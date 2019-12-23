"""  
This game will allow the player to pick wich person goes with the name given
"""

# Clickable images problem solved with this page: https://stackoverflow.com/questions/42577197/pygame-how-to-correctly-use-get-rect
# Shout out to user banana-galaxy on TechWithTim Discord server for finding it

import sqlite3
import pygame as pg
from variable import color, name_var_dict
from pyautogui import size
from speech import speak
from display import display
from random import randrange
from database import get_database
import copy

pg.init()

bgcolor = color['white']
screen = display("Name To Person", size(), bgcolor)

width = size()[0]
height = size()[1]
clock = pg.time.Clock()

data = get_database('family.db','family_info',('rowid','name','gender','relation','image'))
lastans = 0
var_dict = {}
var_dict = copy.deepcopy(name_var_dict)


def showimg(img, x, y):

    img_rect = img.get_rect()
    img_rect.centerx = x
    img_rect.centery = y
    screen.blit(img, img_rect)
    return img

while True:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            if picture.get_rect(center=location).collidepoint(x, y):
                speak('That is the correct answer!')
                var_dict = copy.deepcopy(name_var_dict)
            else:
                speak('Sorry, try again!')

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_g:
                exit()
    screen.fill(bgcolor)

    while len(var_dict['person']) < 3:
        rowid = randrange(len(data)) + 1
        if rowid == lastans:
            var_dict['picked'].append(rowid)
        while rowid in var_dict['picked']:
            rowid = randrange(len(data)) + 1
        var_dict['picked'].append(rowid)
        for entry in data:
            if entry['rowid'] == rowid:
                var_dict['person'].append(entry)
                mem = var_dict['person'][int(len(var_dict['person']) - 1)]
                image = pg.image.load(f'img/{mem["image"]}')
                img_w, img_h = image.get_size()
                image = pg.transform.scale(image,(int(img_w*.25),int(img_h*.25)))
                var_dict['images'].append(showimg(image, (len(var_dict['person'])*width) // 4, height // 4))
                var_dict['center'].append((len(var_dict['person'])*width//4, height//4))
    for x,img in enumerate(var_dict['images']):
        showimg(img, ((x+1)*width)//4, height//4)
    
    pg.display.flip()
    pg.display.update()

    while not var_dict['selected']:
        ans = randrange(3)
        answer = var_dict['person'][ans]
        picture = var_dict['images'][ans]
        location = var_dict['center'][ans]
        print(answer)
        speak(f'which one is {answer["name"]}')
        lastans = answer['rowid']
        var_dict['selected'] = True
    
    clock.tick(30)
