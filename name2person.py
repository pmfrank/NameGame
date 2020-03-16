"""  
This game will allow the player to pick wich person goes with the name given
"""

# Clickable images problem solved with this page: https://stackoverflow.com/questions/42577197/pygame-how-to-correctly-use-get-rect
# Shout out to user banana-galaxy on TechWithTim Discord server for finding it


from variable import color, name_var_dict
from helper_functions import display, get_database, show_img, speak
import pygame as pg
from pyautogui import size
from random import randrange

import copy

pg.init()

bgcolor = color['white']
screen = display("Name To Person", size(), bgcolor)

width, height = size()
clock = pg.time.Clock()

data = get_database('family.db','family_info',('rowid','name','gender','relation','image'))
lastans = 0
var_dict = {}
var_dict = copy.deepcopy(name_var_dict)
playing = True

while playing:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            if picture.get_rect(center=location).collidepoint(x, y):
                speak('That is the correct answer!')
                var_dict = copy.deepcopy(name_var_dict)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_g:
                playing = False
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
                image = pg.transform.scale(image,(int(img_w*.5),int(img_h*.5)))
                var_dict['images'].append(show_img(screen, image, (len(var_dict['person'])*width) // 4, height // 4))
                var_dict['center'].append((len(var_dict['person'])*width//4, height//4))
    for x,img in enumerate(var_dict['images']):
        show_img(screen, img, ((x+1)*width)//4, height//4)
    
    pg.display.flip()
    pg.display.update()

    while not var_dict['selected']:
        ans = randrange(3)
        answer = var_dict['person'][ans]

        pg.display.flip()
        picture = var_dict['images'][ans]
        location = var_dict['center'][ans]
        print(answer)
        speak(f'which one is {answer["name"]}')
        lastans = answer['rowid']
        var_dict['selected'] = True
    
    clock.tick(30)
