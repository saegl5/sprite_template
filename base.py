"""
Sprite Template
"""

import pygame
import src.canvas as canvas # manages and decorates screen
from custom.classes import Rect # constructs sprites
from custom.functions import time_stamp, save_energy # saves energy

pygame.display.set_caption("Sprite")
pygame.key.set_repeat(10) # 10 millisecond delay

WHITE = pygame.Color("white") # optional color
W, H = 64, 64
V = 10 # example
x_inc, y_inc = 0, 0

player = Rect(W, H)
player.rect.x = canvas.SIZE[0]/2 - W/2 # centering
player.rect.y = canvas.SIZE[1]/2 - H/2
player.image.fill(WHITE)
sprites = pygame.sprite.Group()
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            canvas.close()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_inc = -V
            elif event.key == pygame.K_RIGHT:
                x_inc = V
            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                y_inc = -V
            elif event.key == pygame.K_DOWN:
                y_inc = V
        elif event.type == pygame.KEYUP:
            x_inc, y_inc = 0, 0

        time_stamp(event) # takes, if player is idling

    player.rect.x += x_inc
    player.rect.y += y_inc
    # Other game logic

    canvas.clean()
    sprites.draw(canvas.screen)
    canvas.show()

    save_energy() # reduces frame rate, if player is idling