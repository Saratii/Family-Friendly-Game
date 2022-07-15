import pygame
import RotationalBullshitery
import Boss

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
lizzos = []
lizzoTimer = 0

def mainGame(screen, px, py, isFired):
    global lizzoTimer
    lizzoTimer += 1
    if lizzoTimer % 120 == 0:
        lizzos.append(Boss.boss(screen, px, py))
    screen.fill(darkGrey)
    screen.blit(map_image, (0, 0), area=(px - width//2, py-height//2, width, height), special_flags=0)
    screen.blit(panda, pandarect)
    for lizzo in lizzos:
        lizzo.moob()
        lizzo.dwa(px-width//2, py-height//2)
    for bubble in bubbles:
        bubble.moob()
        bubble.dwa(px-width//2, py-height//2)
        if bubble.lifetime < 1:
            bubbles.remove(bubble)
    for bubble in bubbles:
        for lizzo in lizzos:
            if bubble.mask.overlap(lizzo.mask, bubble.offset(bubble, lizzo)):
                bubbles.remove(bubble)
                lizzos.remove(lizzo)
    

    rotGun, rotGunRect = RotationalBullshitery.gunRotate(bubbleGun, isFired)
    screen.blit(rotGun, rotGunRect)
    screen.blit(panda, panda.get_rect())
    


