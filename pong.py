import pygame
import sys
import time
from settings import screen_settings, racket_1_settings


# C'è una palla che si muove da destra a sinistra, ci sono due racchette che la colpiscono muovendo su
# e giu secondo se il giocatore usa la freccia alta o bassa. Quando la palla si scontra torna indietro e
# aumenta la propria velocità. Il tutto continua fino a quando non esce dal campo

screen = screen_settings()
#Coords
racket_1_y = 450
racket_2_y = 450
ball_x = 700
ball_y = 500

#Speed
racket_1_speed = 10
racket_2_speed = 10
ball_speed = 5

pygame.init()

window = pygame.display.set_mode((screen.width, screen.height))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
running = True
start = True
collision_1 = False
collision_2 = False


while running:

    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if racket_1_y > 50 and keys[pygame.K_UP] or keys[pygame.K_w]:
        racket_1_y -= racket_1_speed
    elif racket_1_y < 850 and keys[pygame.K_DOWN] or keys[pygame.K_s]:
        racket_1_y += racket_1_speed

    if racket_1_y != racket_2_y:
        if racket_1_y < racket_2_y:
            racket_2_y -= racket_2_speed
        elif racket_1_y > racket_2_y:
            racket_2_y += racket_2_speed
            
    if start:
        ball_x -= ball_speed

    racket_1 = pygame.draw.rect(window, (255,255,255), (50,racket_1_y,20,100))
    racket_2 = pygame.draw.rect(window, (255,255,255), (1350,racket_2_y,20,100))
    ball = pygame.draw.circle(window, (255,255,255), center=(ball_x,ball_y), radius=(20) )

    if ball.colliderect(racket_1):
        start = False
        collision_2 = False
        ball_x = racket_1.right + 20
        collision_1 = True

    if ball.colliderect(racket_2):
        collision_1 = False
        ball_x = racket_2.left - 20
        collision_2 = True

    if collision_1:
        ball_x += ball_speed
    elif collision_2:
        ball_x -= ball_speed
    if ball_x > 1360 or ball_x < 40:
        print("You loose")
        running = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

