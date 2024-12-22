# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setup clock
    clock = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update Elements
        player.update(dt)

        # Draw Elements
        screen.fill((0,0,0,0))
        player.draw(screen)


        # Refresh display
        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()