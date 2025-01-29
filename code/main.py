import pygame
from os.path import join
from random import randint

#general setup
pygame.init()

# Create a display_surface and give it a width and height
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Setting running variable to true
running = True

#Set Window title
title = "Awesome Game Title"
pygame.display.set_caption(title, "Enjoy!")

#Surface
surf = pygame.Surface((100, 200))
surf.fill("red")
x = 100

#importing an image
star_path = join('images', 'star.png')
star_surf = pygame.image.load(star_path).convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)] # Create tuple to store x and y before the while loop

#Keep the main image(you) on the top of all other images
ship_path = join('images', 'ship.png')
ship_surf = pygame.image.load(ship_path).convert_alpha()

#event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    display_surface.fill('#999999')
    x += 0.1
    for pos in star_pos:
        display_surface.blit(star_surf, pos)
    display_surface.blit(ship_surf, (x, 150))
    pygame.display.update()


# Close the game properly
pygame.quit()
