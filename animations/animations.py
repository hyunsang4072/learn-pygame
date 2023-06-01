import pygame, sys, random as r

class Player(pygame.sprite.Sprite):  # Follow mouse cursor
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("./animations/frog_jump_complete_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/Frog_r_attack_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/frog_r_idle.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_b_attack_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_b_idle_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_g_attack_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_g_idle_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_g_jump_1launch_anim.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_g_jump_2up.gif"))
        self.sprites.append(pygame.image.load("./animations/spr_frog_r_attack_anim.gif"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True
    
    def update(self):
        if self.is_animating:
            # self.current_sprite += 1
            self.current_sprite += 0.3

            # After one animation...
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            # self.image = self.sprites[self.current_sprite]
            self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Create sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()
    

    # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)