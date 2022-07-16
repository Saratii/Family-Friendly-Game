
import pygame
import FamilyFriendlyBubble
import RotationalBullshitery
import Boss

width = 1920
height = 1080
map_image = pygame.image.load("assets/tempMap.jpg")
bubbleGun = pygame.image.load("assets/bubbleGun.png")
panda = pygame.image.load("assets/pandaCharacter.png")
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
score = 0
scoreList = []
purple = (95, 15, 160)
pygame.font.init()
font = pygame.font.SysFont('Helvetica Bold', 80)
with open('save.txt') as f:
    lines = f.readlines()
    for line in lines:
        scoreList.append(line.split(","))
lizzoDifficultyCounter = 100

def mainGame(screen, px, py, isFired, setStatus):
    global lizzoDifficultyCounter
    global lizzoTimer
    global lizzos
    global bubbles
    lizzoTimer += 1
    if lizzoTimer % lizzoDifficultyCounter == 0:
        lizzos.append(Boss.boss(screen, px, py))
        lizzoDifficultyCounter -= 1 if lizzoDifficultyCounter > 1 else 0
    print(len(lizzos))
    screen.fill(darkGrey)
    screen.blit(map_image, (0, 0), area=(px - width//2, py-height//2, width, height), special_flags=0)
    screen.blit(panda, pandarect)
    for lizzo in lizzos:
        lizzo.moob(px, py)
        lizzo.dwa(px-width//2, py-height//2)
        if lizzo.doIBeInPamdasBusiness(px, py):
            setStatus("lizzoed") 
    for bubble in bubbles:
        bubble.moob()
        bubble.dwa(px-width//2, py-height//2)
        if bubble.lifetime < 1:
            bubbles.remove(bubble)
        for lizzo in lizzos:
            if lizzo.doIBeShot(bubble):
                if bubble in bubbles:
                    bubbles.remove(bubble)
                lizzos.remove(lizzo)
                global score
                score += 1
        
    

    rotGun, rotGunRect = RotationalBullshitery.gunRotate(bubbleGun, isFired)
    text = font.render(f'Score: {score}', False, purple)
    text_rect = text.get_rect(center=(200, 100))
    screen.blit(text, text_rect)
    screen.blit(rotGun, rotGunRect)
def reset(px, py):
    global score
    global lizzos
    global bubbles
    global lizzoTimer
    score = 0
    lizzos = []
    bubbles = []
    lizzoTimer = 0
    px = 1920/2
    py = 1080/2
    return px, py

def shoot(screen, bubbles, px, py):
    x, y = pygame.mouse.get_pos()
    dx = x-width/2
    dy = y-height/2
    #print(f'DX {dx} DY {dy} X {x} Y {y}')
    bubbles.append(FamilyFriendlyBubble.Bubble(px, py+10, 15*dx/(dx*dx+dy*dy)**0.5, 15*dy/(dx*dx+dy*dy)**0.5, screen))
    isFired = True
    return isFired
def automatic(screen, bubbles, px, py, timer):
    timer += 1
    if timer % 10 == 0:
        isFired = shoot(screen, bubbles, px, py)
    else: isFired = False
    return isFired, timer
