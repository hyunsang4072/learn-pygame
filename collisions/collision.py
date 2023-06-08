import pygame as pg, sys, random as r

# Initiate
pg.init()

# General Setups
clock = pg.time.Clock()
screen_width, screen_height = 800, 800
screen = pg.display.set_mode((screen_width, screen_height))

# Colors (Red, Green, Blue)
white = 255, 255, 255
red = 255, 0, 0

# Functions
def move_objects():
    global x_speed, y_speed, other_speed

    # Draw objects
    pg.draw.rect(screen, white, moving_rect)
    pg.draw.rect(screen, red, other_rect)

    # Move objects
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    # Check for Out_Of_Bounds
    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
        y_speed *= -1
    
    # Check for Object Collision
    collision_tolerance = 6
    if moving_rect.colliderect(other_rect):
        # 
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1
    
    # Other Rect y-Movement
    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_speed *= -1
    
    # # Other Rect x-Movement
    # other_rect.x += other_speed
    # if other_rect.left <= 0 or other_rect.top >= screen_height:
    #     other_speed *= -1

### random position ALMOST working but unsure what's causing an edge case to happen ###
# moving_randomX = r.randint(0, screen_width - 100)
# moving_randomY = r.randint(0, screen_height - 100)
# moving_rect = pg.Rect(moving_randomX, moving_randomY, 100, 100)

moving_rect = pg.Rect(350, 350, 100, 100)
# 350, 350 for position; 100, 100 for width and height

x_speed, y_speed = 5, 4

### random position ALMOST working but unsure what's causing an edge case to happen ###
# other_randomX = r.randint(0, screen_width - 200)
# other_randomY = r.randint(0, screen_height - 100)
# other_rect = pg.Rect(other_randomX, other_randomY, 200, 100)

other_rect = pg.Rect(300, 600, 200, 100)
other_speed = 2

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()      # same as clicking "x" button
    
    screen.fill((30, 30, 30))

    move_objects()

    pg.display.flip()
    clock.tick(60)      # 60 fps
