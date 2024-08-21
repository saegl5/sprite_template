import pygame

class Rect(pygame.sprite.Sprite): # make it a sprite
    def __init__(self, w, h): # define constructor
        super().__init__() # initialize sprite by calling its parent's constructor
        size = (w, h)
        self.image = pygame.Surface(size, pygame.SRCALPHA) # image is transparent
        self.rect = self.image.get_rect() # pair image with rectangle object