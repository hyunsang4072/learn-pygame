import pygame, sys

class Hairyhair(pygame.sprite.Sprite):
    def __init__(self, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        # self.image.fill(color)
        self.rect = self.image.get_rect()
        # self.rect.center = [pos_x, pos_y]
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# General setup
pygame.init()
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)

# Game screen
screen_width = 1920 // 2
screen_height = 1080 // 2
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background
background = pygame.image.load("Background_Blue.png")
# No mouse showing on gamescreen
pygame.mouse.set_visible(False)

# Creating an instance
hairyhair = Hairyhair("slice56_56.png")

hairyhair_group = pygame.sprite.Group()
hairyhair_group.add(hairyhair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    pygame.display.flip()
    screen.blit(background, (0, 0))
    hairyhair_group.draw(screen)
    
    # Get mouse position and update
    hairyhair_group.update()
    clock.tick(60)