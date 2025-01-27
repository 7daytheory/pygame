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
target_path = join('images', 'target.png')
target_surf = pygame.image.load(target_path).convert_alpha()
football_path = join('images', 'football.png')
football_surf = pygame.image.load(football_path).convert_alpha()
football_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)] # Create tuple to store x and y before the while loop

#event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    display_surface.fill('#999999')
    x += 0.1
    for pos in football_pos:
        display_surface.blit(football_surf, pos)
    display_surface.blit(target_surf, (x, 150))
    pygame.display.update()


# Close the game properly
pygame.quit()
