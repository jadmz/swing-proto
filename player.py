import pygame
from pygame.locals import *


class Player:
    
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.width = 50
        self.height = 50
        self.color = (255,0,0)
        
    def update(self, events):
        self.processEvents(events)

    def processEvents(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.posx += 1
                elif event.key == K_LEFT:
                    self.posx -= 1
                elif event.key == K_DOWN:
                    self.posy += 1
                elif event.key == K_UP:
                    self.posy -= 1
                

    def render(self, windowSurface):
        windowSurface.fill(self.color,
                           (self.posx, self.posy, self.width, self.height))
