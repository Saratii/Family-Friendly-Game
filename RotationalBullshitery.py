import pygame
import math

width, height = 1920, 1080
def gunRotate(image, fired):
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
    rotGun = pygame.transform.rotate(image, angle)
    if x < width/2:
        rotGun = pygame.transform.flip(rotGun, True, False)
    rotGunRect = rotGun.get_rect()
    xOffset = 0
    yOffset = 0
    if fired:
        xOffset, yOffset = gunRecoil(angle)
    rotGunRect.center = (width/2-xOffset, height/2+20-yOffset)
    #print(f'angle {angle} back angle {angle+180}')
    return rotGun, rotGunRect

def gunRecoil(angle):
    x, y = pygame.mouse.get_pos()
    backAngle = (angle+180)*math.pi/180
    if x<width/2 and y < height/2+20:
        x_dir = 10 
        y_dir = 10
    if x>=width/2 and y < height/2+20:
        x_dir = -10
        y_dir = 10  
    if x<width/2 and y >= height/2+20:
        x_dir = 10
        y_dir = 10
    if x>=width/2 and y >= height/2+20:
        x_dir = -10
        y_dir = 10
    
    return x_dir * math.cos(backAngle), y_dir * math.sin(backAngle)