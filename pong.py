import pygame
from settings import screen_settings, racket_1_settings
import random

screen = screen_settings()

#Coords
racket_1_y = 450
racket_2_y = 450
ball_x = 700
ball_y = 500

#Speed
racket_1_speed = 10
ball_speed_x = 8
ball_speed_y = 4

pygame.init()

window = pygame.display.set_mode((screen.width, screen.height))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

running = True
game_over = False
start = True
collision_1 = False
collision_2 = False
up_border_collision = False
low_border_collision = False
left = False
right = False

increase_ball_speed = pygame.USEREVENT + 1
pygame.time.set_timer(increase_ball_speed, 2000)

increase_racket_speed = pygame.USEREVENT + 2
pygame.time.set_timer(increase_racket_speed, 7000)


while running:

    window.fill((0,0,0))

    if game_over:
        racket_1_y = 450
        racket_2_y = 450
        ball_x = 700
        ball_y = 500
        racket_1_speed = 10
        ball_speed_x = 8
        ball_speed_y = 4
        button = pygame.Rect(550,750,300,100)
        pygame.draw.rect(window, (0,200,0), button)
        pos_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.collidepoint(pos_mouse):
                    start = True
                    collision_1 = False
                    collision_2 = False
                    up_border_collision = False
                    low_border_collision = False
                    game_over = False
                

    
    elif not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == increase_ball_speed:
                ball_speed_x += 0.5
                ball_speed_y += 0.5
            elif event.type == increase_racket_speed:
                racket_1_speed += 1

        keys = pygame.key.get_pressed()
        if racket_1_y > 50 and keys[pygame.K_UP] or keys[pygame.K_w]:
           racket_1_y -= racket_1_speed
        elif racket_1_y < 850 and keys[pygame.K_DOWN] or keys[pygame.K_s]:
            racket_1_y += racket_1_speed

        if ball_y != racket_2_y:
            if ball_y < racket_2_y:
                racket_2_y -= ball_speed_y
            elif ball_y > racket_2_y:
                racket_2_y += ball_speed_y
 
        if start:
            ball_x -= ball_speed_x

        racket_1 = pygame.draw.rect(window, (255,255,255), (50,racket_1_y,20,100))
        racket_2 = pygame.draw.rect(window, (255,255,255), (1350,racket_2_y,20,100))
        ball = pygame.draw.circle(window, (255,255,255), center=(ball_x,ball_y), radius=(20) )
        

        if ball.colliderect(racket_1):
            impact_point = ball_y - racket_1_y
            if impact_point < 40:
                d_ball_speed_y = -3
            elif impact_point <= 60:
                d_ball_speed_y = 0
            elif impact_point > 60:
                d_ball_speed_y = 3

            start = False
            collision_2 = False
            up_border_collision = False
            low_border_collision = False
            ball_x = racket_1.right + 20
            collision_1 = True
            left = True

        if ball.colliderect(racket_2):
            number = random.randint(1,2)
            collision_1 = False
            up_border_collision = False
            low_border_collision = False
            ball_x = racket_2.left - 20
            collision_2 = True
            right = True

        if ball_y < 40:
            up_border_collision = True
            collision_1 = False
            collision_2 = False

        if ball_y > 960:
            low_border_collision = True
            collision_1 = False
            collision_2 = False

        if collision_1:
            ball_x += ball_speed_x
            ball_y += d_ball_speed_y
            right = False
    
        if collision_2:
            if number == 1:
                ball_x -= ball_speed_x
                ball_y -= ball_speed_y
                left = False
            elif number == 2:
                ball_x -= ball_speed_x
                ball_y += ball_speed_y
                left = False
            

        if up_border_collision:
            if left:
                ball_x += ball_speed_x
                ball_y += ball_speed_y
            elif right:
                ball_x -= ball_speed_x
                ball_y += ball_speed_y

        if low_border_collision:
            if left:
                ball_x += ball_speed_x
                ball_y -= ball_speed_y
            if right:
                ball_x -= ball_speed_x
                ball_y -= ball_speed_y

    
        if ball_x > 1360 or ball_x < 40:
            game_over = True


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

