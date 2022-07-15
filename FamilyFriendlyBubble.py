import pygame

class Bubble:
    red = (255, 0, 0)
    def __init__(self, posX, posY, velX, velY, screen):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        self.lifetime = 300
        self.screen = screen
    def moob(self):
        self.posX += self.velX
        self.posY += self.velY
        self.lifetime -= 1
    def dwa(self, px, py):
        pygame.draw.circle(self.screen, self.red, (self.posX-px, self.posY-py), 3)