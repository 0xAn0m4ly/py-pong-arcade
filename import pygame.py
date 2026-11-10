import pygame
import sys
from settings import screen_settings


# C'è una palla che si muove da destra a sinistra, ci sono due racchette che la colpiscono muovendo su
# e giu secondo se il giocatore usa la freccia alta o bassa. Quando la palla si scontra torna indietro e
# aumenta la propria velocità. Il tutto continua fino a quando non esce dal campo

window = screen_settings()

pygame.init()
screen = pygame.display.set_mode((window.height, window.width))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            sys.exit()

    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

