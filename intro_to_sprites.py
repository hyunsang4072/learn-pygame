import pygame, sys

class Hairyhair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)

# Game screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

hairyhair = Hairyhair(50, 50, 100, 100, white)

hairyhair_group = pygame.sprite.Group()
hairyhair_group.add(hairyhair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    pygame.display.flip()
    hairyhair_group.draw(screen)
    clock.tick(60)