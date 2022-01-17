import pygame
from pygame.locals import *

import ant


def start():
    # Initialise screen
    window_width = 500
    window_height = 500
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Langton`s Ant with Python')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    w = 250
    h = 250
    scale_width = int(window_width / w)
    scale_height = int(window_height / h)
    field = ant.Field(w, h)
    ants = [
        ant.AntRL(w, h, int(h / 4), int(w / 2), (255, 0, 0)),
        ant.AntRL(w, h, int(h / 3), int(w / 2), (0, 255, 0)),
        ant.AntRL(w, h, int(h / 2), int(w / 2), (0, 0, 255))
    ]
    print(f'ant starts at {ants[0].pos}')

    def cycle():
        for gameEvent in field.tick(ants):
            pygame.draw.rect(
                screen,
                gameEvent[1],
                Rect(
                    gameEvent[0][1] * scale_width,
                    gameEvent[0][0] * scale_height,
                    scale_width,
                    scale_height))

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0

        cycle()

        pygame.display.flip()