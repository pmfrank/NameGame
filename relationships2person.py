from variable import color, name_var_dict
from helper_functions import get_database, speak, display, show_img
from random import shuffle, choice
import pygame as pg
from pyautogui import size

pg.init()

bgcolor = color['white']
screen = display("Relationship To Person", size(), bgcolor)

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

shuffle(guesses)
print(guesses)

height_div = [4,2,1.3]

font = pg.font.SysFont('quicksandmedium', 80)

while True:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            print(x,y)
            print(ans_rect.center)
            print(ans_rect.topleft, ans_rect.bottomright)
            if ans_rect.collidepoint(x,y):
                print('That is the correct answer!')
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    exit()
    screen.fill(bgcolor)

    for x, guess in enumerate(guesses):
        text = font.render(guess, True, color['white'], color['magenta'])
        screen.blit(text, (width//1.3-text.get_width()//2, height//height_div[x]-text.get_height()//2))
        if guess == ans:
            ans_rect = text.get_rect(center=(width//1.3-text.get_width()//2, height//height_div[x]-text.get_height()//2))

    pg.display.flip()

print(ans_rect)