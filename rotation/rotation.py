import pygame as pg, sys

# Colors
white = (255, 255, 255)

# General Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([900, 900])
pikachu = pg.image.load("./rotation/pikachu.png")
pikachu_rect = pikachu.get_rect(center = (450, 450))
angle = 0

def rotate(surface, angle):
    rotated_surface = pg.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center = (450, 450))
    return rotated_surface, rotated_rect

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    angle += 1
    screen.fill(white)
    pikachu_rotated, pikachu_rotated_rect = rotate(pikachu, angle)
    screen.blit(pikachu_rotated, pikachu_rotated_rect)
    pg.display.flip()
    clock.tick(30)