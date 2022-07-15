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


while running:
    clock.tick(60)
    if status == "Menu":
        MenuScreen.Menu(screen)
    elif status == "Playing":
        Game.mainGame(screen, px, py, isFired)
        if framesOnFired > 3:
            isFired = False
            framesOnFired = 0
        if isFired:
            framesOnFired+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pointer = pygame.mouse.get_pos()
            if status == "Menu":
                if MenuScreen.start_button_rect.collidepoint(pointer):
                    status = "Playing"
            elif status == "Playing":
                x, y = pygame.mouse.get_pos()
                dx = x-Game.width/2
                dy = y-Game.height/2
                #print(f'DX {dx} DY {dy} X {x} Y {y}')
                Game.bubbles.append(FamilyFriendlyBubble.Bubble(px, py+10, 15*dx/(dx*dx+dy*dy)**0.5, 15*dy/(dx*dx+dy*dy)**0.5, screen))
                isFired = True
                
        if event.type == pygame.KEYDOWN:
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
