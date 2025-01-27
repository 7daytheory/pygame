import pygame

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

#event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill('#999999')
    x += 0.1
    display_surface.blit(surf, (x, 150))
    pygame.display.update()


# Close the game properly
pygame.quit()