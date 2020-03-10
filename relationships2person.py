from variable import color, name_var_dict
from helper_functions import get_database, speak, display, show_img
from random import shuffle, choice
import pygame as pg
from pyautogui import size

pg.init()

bgcolor = color['white']
screen = display("Name To Person", size(), bgcolor)

width, height = size()
clock = pg.time.Clock()

data = get_database('family.db','family_info',('rowid','name','gender','relation','image'))

relations = ['aunt','uncle','cousin','grandma','grandpa','sister','mom','dad']

shuffle(data)

person = data[0]

ans = person['relation']

guesses = [person['relation']]
print(guesses)

for i in range(2):
    select = choice(relations)
    while select in guesses:
        select = choice(relations)
    guesses.append(select)

print(type(guesses))

# while True:

#     events = pg.event.get()
#     for event in events:
#         if event.type == pg.QUIT:
#             exit()
#         if event.type == pg.MOUSEBUTTONDOWN:
#             x,y = event.pos
#             if picture.get_rect(center=location).collidepoint(x, y):
#                 speak('That is the correct answer!')
#                 var_dict = copy.deepcopy(name_var_dict)

#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_g:
#                 exit()
#     screen.fill(bgcolor)

