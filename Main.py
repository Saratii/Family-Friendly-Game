import re
import pygame
import MenuScreen
import Game
import FamilyFriendlyBubble
import RotationalBullshitery

screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
status = "Menu"
px = 1920/2
py = 1080/2

speed = 5
clock = pygame.time.Clock() 
FPS = 60 
pressed_down = False
pressed_left = False
pressed_right = False
pressed_up = False
running = True
isFired = False
framesOnFired = 0
holdingDown = False
timer = 0

def setStatus(status2):
    global status
    status = status2

while running:
    clock.tick(60)
    if status == "lizzoed":
        MenuScreen.lizzoed(screen)
    elif status == "Menu":
        MenuScreen.Menu(screen)
    elif status == "Playing":
        Game.mainGame(screen, px, py, isFired, setStatus)
        if framesOnFired > 3:
            isFired = False
            framesOnFired = 0
        if isFired:
            framesOnFired+=1
        if holdingDown:
            isFired, timer = Game.automatic(screen, Game.bubbles, px, py, timer)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if holdingDown: 
                holdingDown = False
            else:
                pointer = pygame.mouse.get_pos()
                if status == "Menu":
                    if MenuScreen.start_button_rect.collidepoint(pointer):
                        status = "Playing"
                elif status == "Playing":
                    isFired = Game.shoot(screen, Game.bubbles, px, py)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if status == "Playing":
                holdingDown = True       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pressed_left = True
            elif event.key == pygame.K_d: 
                pressed_right = True
            elif event.key == pygame.K_w:
                pressed_up = True
            elif event.key == pygame.K_s:
                pressed_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pressed_left = False
            elif event.key == pygame.K_d:
                pressed_right = False
            elif event.key == pygame.K_w:
                pressed_up = False
            elif event.key == pygame.K_s:
                pressed_down = False 
            elif event.key == pygame.K_SPACE and status == "lizzoed":
                px, py = Game.reset(px, py)
                status = "Playing"

    if pressed_left:
        px -= speed
    if pressed_right:
        px += speed
    if pressed_up:
        py -= speed
    if pressed_down:
        py += speed
    
    #print(clock.get_fps())
    pygame.display.flip()


