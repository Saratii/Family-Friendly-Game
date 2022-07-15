import math
import pygame

width = 1920
height = 1080
map_image = pygame.image.load("tempMap.jpg")
bubbleGun = pygame.image.load("bubbleGun.png")
panda = pygame.image.load("pandaCharacter.png")
panda = pygame.transform.scale(panda, (100, 100))
bubbleGun = pygame.transform.scale(bubbleGun, (175, 115))
pandarect = panda.get_rect()
bubbleGunRect = bubbleGun.get_rect()
pandarect.center = (width/2, height/2)
bubbleGunRect.center = (width/2, height/2+18)
darkGrey = (47, 47, 47)
bubbles = []

def mainGame(screen, px, py):
    screen.fill(darkGrey)
    screen.blit(map_image, (0, 0), area=(px - width//2, py-height//2, width, height), special_flags=0)
    screen.blit(panda, pandarect)
    for bubble in bubbles:
        bubble.moob()
        bubble.dwa(px-width//2, py-height//2)
        if bubble.lifetime < 1:
            bubbles.remove(bubble)
    x, y = pygame.mouse.get_pos()
    if x == width/2:
        if y>height/2:
            angle = 270
        else:
            angle = 90
    elif x < width/2: 
        angle = math.atan((y-height/2)/(x-width/2)) / math.pi*180
    else:
        angle = math.atan((y-height/2)/(x-width/2)) / math.pi*-180
    rotGun = pygame.transform.rotate(bubbleGun, angle)
    if x < width/2:
        rotGun = pygame.transform.flip(rotGun, True, False)
    rotGunRect = rotGun.get_rect()
    rotGunRect.center = (width/2, height/2+20)
    screen.blit(rotGun, rotGunRect)


