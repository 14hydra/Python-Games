
import pygame
import math

from jtlgames.vector20 import Vector20Factory


"""
1. Open and read `01a_vector_example.py` and run the program.
2. Copy the code to a new file, `01b_vector_assignment.py`
2. Create vector v1 with x = 0 and y = 1 
3. Scale the vector by 10 with multiplication, then rotate it by 90 degrees so
   it points to the right.
4. Draw the vector from the position (5,5) on the grid.
5. Create a new vector v2 by rotating v1 by 90 dregrees, and draw it from the
   ending position of v1 ( which is the return value from the draw_v20()
   function )
6. Continue rotating and drawing until you have drawn a square."""


# Initialize pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vector with Arrow")

# Create a new Vector20 class with customized screen size and scale
Vector20, draw_v20, draw_grid = Vector20Factory(screen_width, screen_height, 20)
draw_grid(screen)

# Create some vectors
v1 = Vector20(0, 1)
v1 = v1.__mul__(10)
v1.rotate(90)


end = draw_v20(screen, Vector20(5, 5), v1)
v2 = v1.rotate(90)

end = draw_v20(screen, end, v2)
v3 = v2.rotate(90)

end = draw_v20(screen, end, v3)
v4 = v3.rotate(90)

end = draw_v20(screen, end, v4)


# Update display
pygame.display.flip()

# Game loop, just pausing so you can see the screen.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
