import pygame

class Bubble:
    red = (255, 0, 0)
    def __init__(self, posX, posY, velX, velY, screen):
        self.mask = pygame.mask.Mask((3, 3), True)
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
    def offset(self, mask1, mask2):
        return int(mask2.xPos - mask1.posX), int(mask2.yPos - mask1.posY)