import pygame as pg
import sys
import pymunk

# Pymunk: 2D Physics Engine
# pip install pymunk to download Pymunk

# Colors
grey = (217, 217, 217)
black = (0, 0, 0)


def create_apple(space, position):
    # Three types of bodies in Pymunk
    # Static: doesn't move but other bodies can interact with this
    # Dynamic: does move and is affected by gravity(physics)
    # Kinematic: moved by Player
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    # Body arguments = (mass, inertia, body_type)
    body.position = position
    shape = pymunk.Circle(body, 80)  # (body_object, radius)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pg.draw.circle(screen, black, (pos_x, pos_y), 80)


def static_ball(space, position):
    # Static Body = no mass, no inertia
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pg.draw.circle(screen, black, (pos_x, pos_y), 50)


pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
space = pymunk.Space()
# Gravity = x,y
space.gravity = (0, 500)

apples = []

balls = []
balls.append(static_ball(space, (250, 600)))
balls.append(static_ball(space, (500, 500)))

# Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))

    screen.fill(grey)
    draw_apples(apples)
    draw_static_ball(balls)

    # Update Physics
    space.step(1/50)
    pg.display.update()
    clock.tick(120)
