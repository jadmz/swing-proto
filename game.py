import pygame, sys
from pygame.locals import *
from player import Player

class Game:
    FRAMES_PER_SECOND = 30
    
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 10)
        self.windowSurface = pygame.display.set_mode((500, 400), 0, 32)
        
        pygame.display.set_caption('Swing Proto')
        clock = pygame.time.Clock()
        clock.tick(self.FRAMES_PER_SECOND)
        self.running = False
        self.player = Player()


    def run(self):
        self.running = True
        while self.running:
            self.loop()
            
    
    def loop(self):
        events = pygame.event.get()
        self.processEvents(events)
        self.update(events)
        self.render()

    def processEvents(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update(self, events):
        self.player.update(events)

    def render(self):
        self.windowSurface.fill((255,255,255))
        self.player.render(self.windowSurface)
        pygame.display.flip()

