import math
import pygame

#Some chaotic system first in 2d then 3d?
#Single pendulum, THen a double, Then with parameters and maybe another graph next to it.

class Pendulum():
    def __init__(self, x, y, size, length, screen_width, screen_height, screen):
        self.x = x
        self.y = y
        self.colour = (0, 0, 255)
        self.size = size
        self.thickness = 1
        self.length = length
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 10
        self.angle =  math.pi / 5
        self.gravity = 9.8281
        self.velocity = 0
        self.damping = 0.99
        self.screen = screen


    def display(self):
        pygame.draw.circle(self.screen, self.colour, ((int(self.screen_width)), (int(self.screen_height))), 5, self.thickness)
        pygame.draw.line(self.screen, self.colour, ((int(self.screen_width)), (int(self.screen_height))), (int(self.x), int(self.y)),self.thickness)
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        self.x = self.length * math.sin(self.angle) + self.screen_width
        self.y = self.length * math.cos(self.angle) + self.screen_height

    def move(self):
        # The length of the arm affects the acceleration greatly that is why we divide by the length of the arm.
        # Play around with the settings.
        # Make a simple version which just changes the angle with a loop see how smooth it runs.
        acceleration = -1 * self.gravity * math.sin(self.angle) / self.length
        self.velocity += acceleration
        self.angle += self.velocity
        self.velocity *= self.damping
