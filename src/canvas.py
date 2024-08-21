import pygame, sys

pygame.init() # initialize submodules that require initialization (e.g., font and mixer)

SIZE = (1024, 640) # example, based on 16:10 resolution
screen = pygame.display.set_mode(SIZE, flags=pygame.SCALED, vsync=1)
BLUE = pygame.Color("blue") # for blue screen
clock = pygame.time.Clock()
fps = 120 # frame rate (max)

def close():
    pygame.quit() # needed for IDLE
    sys.exit()
    
def clean():
    screen.fill(BLUE)

def show():
    pygame.display.flip()
    clock.tick(fps)