import pygame

#general setup
pygame.init()

# Create a display_surface and give it a width and height
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Setting running variable to true
running = True

#event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close the game properly
pygame.quit()