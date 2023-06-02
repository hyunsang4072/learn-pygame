import pygame as pg, sys

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# General Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([800, 800])

# Font
base_font = pg.font.Font(None, 32)
user_text = ''

input_rect = pg.Rect(200, 200, 140, 32)
color_active = pg.Color('lightskyblue3')
color_passive = pg.Color('gray15')
color = color_passive

active = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):  # if you click the input box = can type
                active = True
            else:   # if you click outside the box = cannot type
                active = False

        if event.type == pg.KEYDOWN:
            if active:
                if event.key == pg.K_BACKSPACE:     # delete a word
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    

    screen.fill(black)

    if active:
        color = color_active    # change the input box color
    else:
        color = color_passive   # change the input box color
    
    pg.draw.rect(screen, color, input_rect, 2)

    # Render Input
    text_surface = base_font.render(user_text, True, white)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(150, text_surface.get_width() + 10)

    pg.display.flip()
    clock.tick(60)