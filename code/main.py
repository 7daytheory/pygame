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
player_direction = -1
enemy_x = 50
player_move_speed = 0.5

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

# Store Imported image position/FRects
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)] # Create tuple to store x and y before the while loop
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill(surface_color)
    for pos in star_pos:
        # Add items to display surface
        display_surface.blit(star_surf, pos)
        display_surface.blit(enemy_surf, (enemy_x, 450))
        display_surface.blit(laser_surf, laser_rect)

#Add Player last to display_surfcae - so it's always on top
    player_rect.x += player_direction * player_move_speed
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1  # It will go from left to right if you multiply it by -1 (swaps -1 to positive, and 1 to negative)
    display_surface.blit(player_surf, player_rect)

#Update everything added to pygame display
    pygame.display.update()

# Close the game properly
pygame.quit()
