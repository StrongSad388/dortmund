import pygame

class Image():
    black = (0,0,0)
    white = (255,255,255)

    def __init__(self, imageSource, root, x = 0, y = 0):
        self.imageSource = imageSource
        self.image = None
        self.x = x
        self.y = y
        self.hide = True
        # pygame display object
        self.root = root

    def load(self):
        self.image = pygame.image.load(self.imageSource)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def blit(self, display):
        if not self.hide:
            self.root.blit(self.image, (self.x, self.y))
        pass

