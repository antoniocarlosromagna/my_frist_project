import pygame 
from pygame.locals import * 
from sys import exit 
from random import randint

pygame.init() 

pygame.display.set_caption('rectangle game')
x_px   = 1280
y_px   = 720
screen = pygame.display.set_mode ((x_px, y_px)) # screen resolution 
font   = pygame.font.SysFont('arial', 40, False, False) # fomt 

# rectangle blue spaw location 
x_b = 640 
y_b = 360 

# rectangle red spaw location 
x_r = 780 
y_r = 570 

score = 0 # score of points 

# principal loop 
while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit() 
            exit() 
    screen.fill((0, 0, 0)) # secreen fill

    tx = f'score:{score}' # the text of my message 
    mess = font.render(tx, False, (0, 200, 0)) # message  
    screen.blit(mess, (1100, 40)) # where my message will appears

    # rectangle blue 
    rec_b = pygame.draw.rect(screen, (0, 0, 200), (x_b, y_b, 90, 90))
    
    # rectangle red  
    rec_r = pygame.draw.rect(screen, (200, 0, 0), (x_r, y_r, 90, 90)) 

    # keys moviment of rectangle blue 
    if pygame.key.get_pressed()[K_a]: 
        x_b = x_b - 1
    if pygame.key.get_pressed()[K_d]: 
        x_b = x_b + 1     
    if pygame.key.get_pressed()[K_w]: 
        y_b = y_b - 1
    if pygame.key.get_pressed()[K_s]:    
        y_b = y_b + 1
    
    # limit border 
    if x_b > 1190: 
        x_b = 1190
    if x_b < 0: 
        x_b = 0 
    if y_b > 630:
        y_b = 630
    if y_b < 0: 
        y_b = 0
    
    # colision 
    if rec_b.colliderect(rec_r):
        x_r = randint(0, 1190) 
        y_r = randint(0, 630)
        score = score + 1

    pygame.display.update()  