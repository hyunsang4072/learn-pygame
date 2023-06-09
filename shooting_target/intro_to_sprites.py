import pygame, sys, random as r

class Hairyhair(pygame.sprite.Sprite):  # Follow mouse cursor
    def __init__(self, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        # self.image.fill(color)
        self.rect = self.image.get_rect()
        # self.rect.center = [pos_x, pos_y]
        # Get gunshot sound
        self.gunshot = pygame.mixer.Sound("./shooting_target/lmg_fire01.mp3")
    
    # Add shooting action
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(hairyhair, target_group, True)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, pic_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Colors
# white = (255, 255, 255)

# Game screen
screen_width = 1920 // 2 - 300
screen_height = 1080 // 2 - 100
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background
background = pygame.image.load("./shooting_target/Background_Blue.png")
# No mouse showing on gamescreen
pygame.mouse.set_visible(False)

# Creating an instance
hairyhair = Hairyhair("./shooting_target/slice56_56.png")

hairyhair_group = pygame.sprite.Group()
hairyhair_group.add(hairyhair)

# Target
target_group = pygame.sprite.Group()
for target in range(10):
    new_target = Target("./shooting_target/DuckYellow_3.png", r.randrange(0, screen_width), r.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hairyhair.shoot()
    
    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    hairyhair_group.draw(screen)
    
    # Get mouse position and update
    hairyhair_group.update()
    clock.tick(60)