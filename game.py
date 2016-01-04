import pygame_sdl2, sys

from pygame_sdl2.locals import *
from player import Player
from Box2D import (b2World, b2AABB)

class Game:
    FRAMES_PER_SECOND = 30
    
    def __init__(self):
        pygame_sdl2.init()
        pygame_sdl2.key.set_repeat(1, 10)
        self.windowSurface = pygame_sdl2.display.set_mode((500, 400), 0, 32)
        
        pygame_sdl2.display.set_caption('Swing Proto')
        clock = pygame_sdl2.time.Clock()
        clock.tick(self.FRAMES_PER_SECOND)
        self.running = False
        self.world = b2World(gravity=(0, -10), doSleep=True)
        self.player = Player(self.world)


    def run(self):
        self.running = True
        while self.running:
            self.loop()
            
    
    def loop(self):
        events = pygame_sdl2.event.get()
        self.processEvents(events)
        self.update(events)
        self.render()

    def processEvents(self, events):
        for event in events:
            if event.type == QUIT:
                pygame_sdl2.quit()
                sys.exit()

    def update(self, events):
        self.player.update(events)

    def render(self):
        self.windowSurface.fill((255,255,255))
        self.player.render(self.windowSurface)
        pygame_sdl2.display.flip()

