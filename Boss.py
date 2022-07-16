import random

import Game
import pygame

bossImage = pygame.image.load("assets/EpicBoss.png")
bossImage = pygame.transform.scale(bossImage, (300, 200))
bossRect = bossImage.get_rect()

class boss:      
    def __init__(self, screen, px, py):
        self.mask = pygame.mask.from_surface(bossImage)
        self.screen = screen
        self.vel = 4
        self.px = px
        self.py = py
        self.randomSide = random.randint(0, 1)
        if self.randomSide == 1:
            self.xPos = random.randint(-2000, -100)
        else:
            self.xPos = random.randint(4000, 6000)
        self.randomSide = random.randint(0, 1)
        if self.randomSide == 1:
            self.yPos = random.randint(-2000, -100)
        else:
            self.yPos = random.randint(3000, 5000)
        
    def moob(self, px, py):
        if self.xPos < px - 300:
            self.xPos += self.vel
        if self.xPos > px - 300 :
            self.xPos -= self.vel
        if self.yPos < py - 200:
            self.yPos += self.vel
        if self.yPos > py - 200:
            self.yPos -= self.vel
    def dwa(self, px, py):
        if self.xPos+150 < px:
            self.screen.blit(pygame.transform.flip(bossImage, True, False), (self.xPos-px+150, self.yPos-py+100))
        else:
            self.screen.blit(bossImage, (self.xPos-px+150, self.yPos-py+100)) 
        
    def doIBeShot(self, bubble):
        if bubble.posX -3 > self.xPos + 150 and bubble.posX+3 < self.xPos + 450 and \
           bubble.posY -3 > self.yPos + 100 and bubble.posY+3 < self.yPos + 300:
           return True
        return False
    def doIBeInPamdasBusiness(self, px, py):
        if px -50 > self.xPos + 150 and px+50 < self.xPos + 450 and \
           py -50 > self.yPos + 100 and py+50 < self.yPos + 300:
           return True
        return False