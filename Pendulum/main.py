import Pendulum
import pygame

def main():
    background_colour = (255, 255, 255)
    width, height = (700, 700)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pendulum')

    clock = pygame.time.Clock()
    running = True
    pendulum = Pendulum(350, 390, 10, 100, width/2 , height/2, screen)
    while running:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        else:
            screen.fill(background_colour)
            pendulum.pivot()
            pendulum.display()
            pendulum.move()
           # in a real game use .update() which is less taxing.
            pygame.display.flip()

if __name__ == "__main__":
    main()