import pygame
import sys
import math
from screens import *
from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.win = WIN

    def run(self):
        clock = pygame.time.Clock()

        while True:
            start_screen(self.win)

            scores = [0, 0]

            left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
            right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
            ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
            ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]

            current_paddle_speed = PADDLE_SPEED
            current_ball_vel = ball_vel[:]
            last_speedup_time = pygame.time.get_ticks()

            countdown_screen(WIN, [left_paddle, right_paddle], ball, scores, 3)

            running = True
            while running:
                clock.tick(60)
                now = pygame.time.get_ticks()
                if now - last_speedup_time >= BALL_SPEEDUP_INTERVAL:
                    current_ball_vel[0] *= BALL_SPEEDUP_FACTOR
                    current_ball_vel[1] *= BALL_SPEEDUP_FACTOR
                    current_paddle_speed *= BALL_SPEEDUP_FACTOR
                    last_speedup_time = now

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and left_paddle.top > 0:
                    left_paddle.y -= int(current_paddle_speed)
                if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
                    left_paddle.y += int(current_paddle_speed)
                if keys[pygame.K_UP] and right_paddle.top > 0:
                    right_paddle.y -= int(current_paddle_speed)
                if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
                    right_paddle.y += int(current_paddle_speed)

                ball.x += int(current_ball_vel[0])
                ball.y += int(current_ball_vel[1])

                if ball.top <= 0 or ball.bottom >= HEIGHT:
                    current_ball_vel[1] = -current_ball_vel[1]

                if ball.colliderect(left_paddle):
                    rel = ((ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2))
                    rel = max(-1, min(1, rel))
                    angle = rel * 45
                    speed = (current_ball_vel[0] ** 2 + current_ball_vel[1] ** 2) ** 0.5
                    current_ball_vel[0] = abs(speed * math.cos(math.radians(angle)))
                    current_ball_vel[1] = speed * math.sin(math.radians(angle))
                elif ball.colliderect(right_paddle):
                    rel = ((ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2))
                    rel = max(-1, min(1, rel))
                    angle = rel * 45
                    speed = (current_ball_vel[0] ** 2 + current_ball_vel[1] ** 2) ** 0.5
                    current_ball_vel[0] = -abs(speed * math.cos(math.radians(angle)))
                    current_ball_vel[1] = speed * math.sin(math.radians(angle))

                if ball.left <= 0:
                    scores[1] += 1
                    if scores[1] < WIN_SCORE:
                        ball.center = (WIDTH // 2, HEIGHT // 2)
                        left_paddle.centery = HEIGHT // 2
                        right_paddle.centery = HEIGHT // 2
                        current_ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]
                        current_paddle_speed = PADDLE_SPEED
                        last_speedup_time = pygame.time.get_ticks()
                        countdown_screen(WIN, [left_paddle, right_paddle], ball, scores, 2)

                if ball.right >= WIDTH:
                    scores[0] += 1
                    if scores[0] < WIN_SCORE:
                        ball.center = (WIDTH // 2, HEIGHT // 2)
                        left_paddle.centery = HEIGHT // 2
                        right_paddle.centery = HEIGHT // 2
                        current_ball_vel = [-BALL_SPEED_X, BALL_SPEED_Y]
                        current_paddle_speed = PADDLE_SPEED
                        last_speedup_time = pygame.time.get_ticks()
                        countdown_screen(WIN, [left_paddle, right_paddle], ball, scores, 2)

                draw(WIN, [left_paddle, right_paddle], ball, scores)

                if scores[0] >= WIN_SCORE:
                    game_over_screen(WIN, 1)
                    running = False
                elif scores[1] >= WIN_SCORE:
                    game_over_screen(WIN, 2)
                    running = False