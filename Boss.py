import random
import Game
import pygame

bossImage = pygame.image.load("EpicBoss.png")
bossImage = pygame.transform.scale(bossImage, (300, 200))
bossRect = bossImage.get_rect()

class boss:      
    def __init__(self, screen, px, py):
        self.mask = pygame.mask.from_surface(bossImage)
        self.screen = screen
        self.vel = 5
        self.px = px
        self.py = py
        self.randomSide = random.randint(0, 1)
        if self.randomSide == 1:
            self.xPos = random.randint(-2000, 1000)
        else:
            self.xPos = random.randint(3000, 6000)
        self.randomSide = random.randint(0, 1)
        if self.randomSide == 1:
            self.yPos = random.randint(-2000, 1000)
        else:
            self.yPos = random.randint(3000, 6000)
        
    def moob(self):
        if self.xPos-self.px < Game.width/2:
            self.xPos += self.vel
        if self.xPos-self.px > Game.width/2:
            self.xPos -= self.vel
        if self.yPos-self.py < Game.height/2:
            self.yPos += self.vel
        if self.yPos-self.py > Game.height/2:
            self.yPos -= self.vel
    def dwa(self, px, py):
        if self.xPos < Game.width//2:
            self.screen.blit(pygame.transform.flip(bossImage, True, False), (self.xPos-px+150, self.yPos-py+100))
        else:
            self.screen.blit(bossImage, (self.xPos-px+150, self.yPos-py+100)) 
        

 