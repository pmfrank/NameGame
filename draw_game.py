import pygame as pg
from pygame.color import Color
from pyautogui import size
from helper_functions import display
from classes import Button


def main():
    pg.init()
    screen = display("Drawing",size(),Color('white'),fullscreen=True)
    width, height = size()
    playing = True

    #Color buttons
    black = Button(Color('black'), 10,10, 50, 50)
    black.draw(screen, outline=Color('black'))
    white = Button(Color('white'), 10, 60, 50, 50)
    white.draw(screen, outline=Color('black'))
    red = Button(Color('red'), 10, 110, 50, 50)
    red.draw(screen, outline=Color('black'))
    blue = Button(Color('blue'), 10, 160, 50, 50)
    blue.draw(screen, outline=Color('black'))
    green = Button(Color('green'), 10, 210, 50, 50)
    green.draw(screen, outline=Color('black'))
    yellow = Button(Color('yellow'), 10, 260, 50, 50)
    yellow.draw(screen, outline=Color('black'))
    magenta = Button(Color('magenta'), 10, 310, 50, 50)
    magenta.draw(screen, outline=Color('black'))
    cyan = Button(Color('cyan'), 10, 360, 50, 50)
    cyan.draw(screen, outline=Color('black'))

    quit_button = Button(Color('red'),(width - 300),(height - 150), 200, 75, text='Quit')
    quit_button.draw(screen)
    pg.display.flip()

    color = 'black'

    while playing:
        left_pressed, middle_pressed, right_pressed = pg.mouse.get_pressed()

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit(0)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    playing = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if black.is_over(pos):
                    color = 'black'
                if white.is_over(pos):
                    color = 'white'
                if red.is_over(pos):
                    color = 'red'
                if green.is_over(pos):
                    color = 'green'
                if blue.is_over(pos):
                    color = 'blue'
                if yellow.is_over(pos):
                    color = 'yellow'
                if magenta.is_over(pos):
                    color = 'magenta'
                if cyan.is_over(pos):
                    color = 'cyan'
                if quit_button.is_over(pos):
                    playing = False
            if left_pressed:
                pg.draw.circle(screen, Color(color), (pg.mouse.get_pos()),5)
        pg.display.flip()

if __name__ == "__main__":
    main()