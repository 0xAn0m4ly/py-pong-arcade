import pygame
import sys
from settings import screen_settings


# C'è una palla che si muove da destra a sinistra, ci sono due racchette che la colpiscono muovendo su
# e giu secondo se il giocatore usa la freccia alta o bassa. Quando la palla si scontra torna indietro e
# aumenta la propria velocità. Il tutto continua fino a quando non esce dal campo

window = screen_settings()
pygame.init()

screen = pygame.display.set_mode((window.width, window.height))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
running = True

asse_y_racket_1 = 450

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                asse_y_racket_1 -= 100
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                asse_y_racket_1 += 100

    screen.fill((0, 0, 0))

    # Racchetta
    racket_1 = pygame.draw.rect(screen, (255,255,255), (50,asse_y_racket_1,20,100))
    racket_2 = pygame.draw.rect(screen, (255,255,255), (1350,450,20,100))
    ball = pygame.draw.circle(screen, (255,255,255), center=(700,500), radius=(20) )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

