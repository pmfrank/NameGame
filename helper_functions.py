def show_img(screen, img, x, y):

    img_rect = img.get_rect()
    img_rect.centerx = x
    img_rect.centery = y
    screen.blit(img, img_rect)
    return img