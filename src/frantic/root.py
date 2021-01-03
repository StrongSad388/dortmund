#!/usr/bin/env python3

import pygame


class Root():

    def __init__(self, height = 800, width = 600, fps = 60, caption = ''):
        self.height = height
        self.width = width
        self.fps = fps
        self.finishLoop = False
        self.caption = caption
        pygame.init()
        self.root = pygame.display.set_mode((self.height, self.width))
        pygame.display.set_caption(self.caption)


    def loop(self):

        self.clock = pygame.time.Clock()
        while not self.finishLoop:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    self.finishLoop = True
            print(event)
            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()
        return

if __name__ == '__main__':
    root = Root(height = 1920, width = 1080)
    root.loop()
