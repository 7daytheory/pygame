﻿# Creating Games with Python and Pygame

Requirements
pygame

## What does Pygame do?
https://www.pygame.org/docs/

Draw images and play sounds
Get user inputs
Get and Set positions
Get time, collisions, transform images, color etc
<strong> Easy to learn </strong>

Con:
Has a limited toolset like Godot or Unity

### Pygame vs Pygame-ce (Community Edition)
Pygame-ce is better because it has :
More features
Bigger Community
Gets Updated
Runs better
Fully compatible with pygame

Install pygame-ce
```bash
pip install pygame-ce
```
<italic>ni = npm install</italic>

## Display Surface
The canvas that everything will be drawn on, you can only have one at a time.

## Event Loop
Checks Events - (Click, keyboard, controller input, timers) , keys to start or close game

## Display Surface vs Surface
### Display Surface
Definition: The display surface represents the main window or screen where everything in your game is drawn and displayed to the user.
Purpose: It acts as the "canvas" that the user sees on their screen.
Created Using: pygame.display.set_mode()
Characteristics:
It's the only surface that is actually displayed on the screen.
You cannot create multiple display surfaces—there can only be one.
After drawing or blitting (copying) content to the display surface, you need to call pygame.display.update() or pygame.display.flip() to render it on the screen.
Example of display surface:
```bash
display_surface = pygame.display.set_mode((800, 600))  # Creates the main window
```
### General Surface
Definition: A general surface is an off-screen image or canvas that can hold graphical content (e.g., images, shapes, or text).

Purpose: These surfaces are used as intermediate steps for creating or manipulating graphics before drawing them onto the display surface.

Created Using: pygame.Surface()

Characteristics:

You can create multiple general surfaces.
These surfaces are not directly visible to the user.
They are used for tasks like storing images, rendering temporary graphics, or performing off-screen drawing (e.g., creating a "background" or a "sprite").
Once a general surface is ready, you can copy it onto the display surface using blit.
Example of a general surface:
```bash
my_surface = pygame.Surface((200, 200))  # Create a surface of size 200x200
my_surface.fill((255, 0, 0))  # Fill the surface with red color
```

### Adding a Surface to a Display Surface
The surface was created using pygame.Surface((100, 200)), representing an off-screen canvas of 100x200 pixels. This surface was added to the display_surface (the main screen) using the blit method: display_surface.blit(surface_variable, (100, 150)). The blit function places the surface at coordinates (100, 150) on the display_surface, making it visible when pygame.display.update() is called.

### Adding an image to surface
Using PNG Files in Pygame
PNG is a raster (pixel-based) format and is natively supported by Pygame, making it a more straightforward choice for most use cases. You should probably just go with a PNG unless you realy need the size to change often, or based on resolution

Using SVG Files in Pygame
Pygame does not natively support SVG rendering (since SVGs are vector graphics and Pygame primarily works with raster graphics). However, you can still use SVGs in Pygame by rendering them as rasterized images (e.g., converting them to PNG or directly rendering them using libraries like cairosvg or svg).

## Importing
The file path can become a problem depending on the code editor. <strong>VS Code</strong> starts a relative path from the main directory while <strong>Sublime</strong> and other editors starts from the python file.
So in VS Code the url would be images/image_name.png if you're in the main folder while in sublime it would be ../images/image_name.png

Depending on your OS you might need a different slash in the file path - images/image_name.png or images\player.png.
You should make the paths dynamic

When importing an image, you want to convert it to a format that Pygame can work more easily. 
If the image has no transparent pixels : .convert()
If the image has transparent pixesl: convert_alpha()
This will make the game run much faster

### Display order
The display order is important, in this example there's a background fill, a target that moves and a bunch of random footballs. If the background was created last we would only see the background.
So we want the target on top of everything, so it should be the last thing drawn on the display canvas, and the background should be the first thing drawn.

## Rects
Places surfaces more elegantly
Detect collisions
Can be drawn

### Placing Surfaces Sucks
Since we always place the topleft it requires math to place it in a precist spot
Sometimes we just need to place the center or the right side of a surface
Rects can do this very well

Rects are hyst rectangles with a size and a position
They also have a lot of points :
<strong>Tuples</stronhg> of an x and y position
X or y positions
There is aldo width, height, and size
Each point can be measured and changed
The points stay relative to each other - moving one you move all

positions: topleft, midtop, topright, midright, bottomright, midbottom, bottomleft, midleft
top, right, bottomn, left

## 2 kinds of Rects
### Rects and FRects

They are nearly identical, the only difference is that FRects store data as floating point values while Rects use integers
FRects are usually better since they are more precise

Small Example:
When moving player(ship) from left to right side we add it's value by 0.1 per frame
frect will do this as expected
rect will not because it is just an int and does not accept decimals so the 0.1 value getting added to it will get cancelled out every time

### Creating Rects
You can create a rect from scratch
pygame.Rect(pos, size)
pygame.FGame(post, size)

Or you can create it from a surface (which is much more common):
rect will have the game size as surface
surface.get_rect(point = pos)
surface.get_freact(point = pos)

