import pygame
from os.path import join
from random import randint

#general setup
pygame.init()

# Global Variable
    #Window Width and Height, and color
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
surface_color = "#888888"
    #Enemy X value, Player Move speed
enemy_x = 50
player_move_speed = 0.2

#Display Surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Set game running to true
running = True

#Set Window title
title = "Awesome Game Title"
pygame.display.set_caption(title, "Enjoy!")

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
    display_surface.fill(surface_color)
    for pos in star_pos:
        display_surface.blit(star_surf, pos)
    display_surface.blit(enemy_surf, (enemy_x, 450))
    player_rect.left += player_move_speed
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect)
    pygame.display.update()


# Close the game properly
pygame.quit()
