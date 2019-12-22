import pygame as pg
pg.init()


pg.display.set_caption('This is really pissing me off')
screen = pg.display.set_mode((1000,1000))
screen.fill((255,255,255))
pg.display.flip()
pg.display.update()

pic = pg.image.load('../img/amy.JPG').convert()
screen.blit(pic,(100,30))
pg.display.flip()

while True:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            if pic.get_rect(topleft=(100,30)).collidepoint(x, y):
                print('Clicked on image')
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()