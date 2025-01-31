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

#Display Surface
surf = pygame.Surface((100, 200))
surf.fill("red")
enemy_x = 50
x = 100

#Import Images
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
enemy_surf = pygame.image.load(join("images", "enemy.png")).convert_alpha()
laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()

# Store Imported image position
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)] # Create tuple to store x and y before the while loop
    #FRects
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

#event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    display_surface.fill('#999999')
    for pos in star_pos:
        display_surface.blit(star_surf, pos)
    display_surface.blit(enemy_surf, (enemy_x, 450))
    player_rect.left += 0.2
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect)
    pygame.display.update()


# Close the game properly
pygame.quit()
