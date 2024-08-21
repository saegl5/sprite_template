import pygame
import src.canvas as canvas

ticks = int()

def time_stamp(event):
    global ticks
    if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP or \
        event.type is not pygame.MOUSEMOTION:
        ticks = pygame.time.get_ticks()

def save_energy():
    if pygame.time.get_ticks() - ticks >= 15000: # after at least 15 seconds
        canvas.clock.tick(1) # minimize frame rate