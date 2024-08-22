"""
Sprite Template
"""

import pygame
import src.canvas as canvas # manages and decorates screen
from custom.classes import Rect # constructs sprites
from custom.functions import time_stamp, save_energy # saves energy

pygame.display.set_caption("Sprite")
pygame.key.set_repeat(10) # 10 millisecond delay

player_frames = pygame.image.load('images/female_tilesheet.png').convert_alpha()
W = player_frames.get_width()/9 # tile sheet has nine columns
H = player_frames.get_height()/3 # tile sheet has three rows
frame = [ (W*5, H*2, W, H), # standing
          (W*0, H*1, W, H), # walk1
          (W*1, H*1, W, H), # walk2
          (W*5, H*0, W, H), # climb1
          (W*6, H*0, W, H), # climb2
          (W*1, H*0, W, H) ] # jump
V = 5 # example
x_inc, y_inc = 0, 0
flip = bool() # player face leftward
count = 0 # player walk or climb

player = Rect(W, H)
player.image.blit(player_frames, (0, 0), frame[0]) 
player.rect.x = canvas.SIZE[0]/2 - W/2 # centering
player.rect.y = canvas.SIZE[1]/2 - H/2
sprites = pygame.sprite.Group()
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            canvas.close()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_inc = -V
                flip = True
                count += 1
                if count % 20 == 0:
                    player.image.fill(pygame.Color(canvas.BLUE))
                    player.image.blit(player_frames, (0, 0), frame[1])
                    player.image = pygame.transform.flip(player.image, flip_x=flip, flip_y=False)
                elif count % 10 == 0:
                    player.image.fill(pygame.Color(canvas.BLUE))
                    player.image.blit(player_frames, (0, 0), frame[2])
                    player.image = pygame.transform.flip(player.image, flip_x=flip, flip_y=False)
            elif event.key == pygame.K_RIGHT:
                x_inc = V
                flip = False
                count += 1
                if count % 20 == 0:
                    player.image.fill(pygame.Color(canvas.BLUE))
                    player.image.blit(player_frames, (0, 0), frame[1])
                    player.image = pygame.transform.flip(player.image, flip_x=flip, flip_y=False)
                elif count % 10 == 0:
                    player.image.fill(pygame.Color(canvas.BLUE))
                    player.image.blit(player_frames, (0, 0), frame[2])
                    player.image = pygame.transform.flip(player.image, flip_x=flip, flip_y=False)
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