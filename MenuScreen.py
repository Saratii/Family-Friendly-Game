import pygame
import Game

start_button_rect = pygame.Rect(1920/2-300, 1080/2-150, 600, 300)
pygame.font.init()
font = pygame.font.SysFont('Helvetica Bold', 220)
background = pygame.image.load("assets/blue_gradient.jpg")

def Menu(screen):
    lighter_purple = (115, 35, 180)
    purple = (95, 15, 160)

    pygame.display.set_caption("Menu Screen")
    screen.blit(background, (0, 0))

    buttonColor = purple
    
    pointer = pygame.mouse.get_pos()
    if start_button_rect.collidepoint(pointer):
        buttonColor = lighter_purple
    text = font.render('Play', False, buttonColor)
    text_rect = text.get_rect(center=(1920/2, 1080/2))
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, buttonColor, start_button_rect,  14, 30, 30)

def lizzoed(screen):
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (95, 15, 160), pygame.Rect(1920/2-300, 1080/2-150, 600, 300))
    purple = (95, 15, 160)
    buttonColor = purple
    text = font.render(f'Score: {Game.score}', False, (255, 255, 255))
    text_rect = text.get_rect(center=(1920/2, 1080/2))
    screen.blit(text, text_rect)
