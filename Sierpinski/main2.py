import pygame
import math
import random

black = [0, 0, 0]
size = [1400,1000]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sierpinski")

done = False

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill([255, 255, 255])

    def drawTriangle(x, y, length, screen, color, width):

        top = y - (((3**0.5)/2)*length)
        pygame.draw.line(screen, color, [x, y], [x+length, y] ,width)
        pygame.draw.line(screen, color, [x, y], [x+length/2, top] ,width)
        pygame.draw.line(screen, color, [x+length, y], [x+length/2, top], width)
        #Update screen with drawing.
        pygame.display.flip()



    drawTriangle(300, 400, 100, screen, black, 1)
    drawTriangle(300+100, 400, 100, screen, black, 1)
    drawTriangle(300+50, (400 - (((3**0.5/2)*100))), 100, screen, black, 1)

    clock.tick(144)


pygame.quit()


