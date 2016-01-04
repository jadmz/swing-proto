import pygame_sdl2

from pygame_sdl2.locals import *
from Box2D import (b2EdgeShape, b2FixtureDef, b2PolygonShape, b2RopeJointDef)


class Player:
    
    def __init__(self, world):
        self.posx = 0
        self.posy = 0
        self.width = 50
        self.height = 50
        self.color = (255,0,0)
        self.shape = b2PolygonShape(box=(0.5, 0.125))
        self.shape.box = (1.5, 1.5)
        self.body = world.CreateDynamicBody(
            position = (self.posx, self.posy)
            )
        
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
