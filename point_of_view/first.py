import pygame as pg
import sys

# Colors
white = (255, 255, 255)
black = (30, 30, 30)
red = (255, 0, 0)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((100, 100))
        # if you want to add an image for your player or bullet,
        # self.image = pg.image.load(image_file_path) and no need to self.image.fill(color)
        self.image.fill(white)
        self.rect = self.image.get_rect(
            center=(screen_width / 2, screen_height / 2))

    def update(self):
        self.rect.center = pg.mouse.get_pos()

    def create_bullet(self):
        # (x, y)
        return Bullet(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])


class Bullet(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pg.Surface((50, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        # Bullet Speed
        self.rect.x += 12.5

        # Bullet Out of Bounds
        # If too many bullets, the game will break!!!
        if self.rect.x >= screen_width + 50:
            # Destroy Bullet
            self.kill()


# Basics
pg.init()
clock = pg.time.Clock()
screen_width, screen_height = 800, 800
screen = pg.display.set_mode((screen_width, screen_height))
pg.mouse.set_visible(False)

# Instantiate Player
player = Player()
player_group = pg.sprite.Group()
player_group.add(player)

bullet_group = pg.sprite.Group()

# Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    # Drawing
    screen.fill(black)
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    pg.display.flip()

    # fps: how many times of this while loop per SECOND
    clock.tick(60)
