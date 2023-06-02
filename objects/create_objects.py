import pygame as pg, sys


# General Setup
pg.init()
clock = pg.time.Clock()

# Colors
white = (255, 255, 255) # RGB
blue = (0, 0, 255)

# Create display surface
screen = pg.display.set_mode((800, 800))    # width, height
second_screen = pg.Surface([100, 200])
second_screen.fill(blue)

cat = pg.image.load("./objects/cat.png")
cat_rect = cat.get_rect(topleft = [100, 200])


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:   # QUIT = clicking the exit('x') button
            pg.quit()
            sys.exit()
    
    screen.fill(white)
    screen.blit(second_screen, (0, 50))     # x, y coordinates; (0, 0) = leftTop corner
    screen.blit(cat, cat_rect)
    cat_rect.right += 5
    if cat_rect.right % 100:
        cat_rect.top += 100
    else:
        cat_rect.top = 100
    pg.display.flip()
    clock.tick(60)    # run this while loop 60 times per second