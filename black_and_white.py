import pygame, sys

# Setting up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# how long has it been
current_time = 0
# when you press any button
button_press_time = 0

# setting colors
white = (255, 255, 255)
black = (0, 0, 0)
random_color = (13, 77, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            # fill screen with WHITE color
            screen.fill(white)


    current_time = pygame.time.get_ticks()
    # print(current_time)

    if current_time - button_press_time > 2000:
        screen.fill(black)
    

    # print(f"current time: {current_time} button press time: {button_press_time}")
    pygame.display.flip()
    clock.tick(60)