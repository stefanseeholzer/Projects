import pygame
import sys
from config import *

def draw(win, paddles, ball, scores):
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, paddles[0])
    pygame.draw.rect(win, WHITE, paddles[1])
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_text = SCORE_FONT.render(f"{scores[0]}   {scores[1]}", True, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()

def start_screen(win):
    win.fill(BLACK)
    title = TITLE_FONT.render("PONG", True, WHITE)
    info1 = INFO_FONT.render("First to 10!", True, WHITE)
    info2 = INFO_FONT.render("Press SPACE to Start", True, WHITE)
    win.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    win.blit(info1, (WIDTH // 2 - info1.get_width() // 2, HEIGHT // 2))
    win.blit(info2, (WIDTH // 2 - info2.get_width() // 2, HEIGHT // 2 + 40))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def countdown_screen(win, paddles, ball, scores, seconds):
    for i in range(seconds, 0, -1):
        draw(win, paddles, ball, scores)
        count_text = TITLE_FONT.render(str(i), True, RED)
        info = INFO_FONT.render("Get Ready!", True, RED)
        win.blit(count_text, (WIDTH // 2 - count_text.get_width() // 2, HEIGHT // 2 - 120))
        win.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.flip()
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 1000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

def game_over_screen(win, winner):
    win.fill(BLACK)
    win_text = TITLE_FONT.render(f"Player {winner} Wins!", True, WHITE)
    info = INFO_FONT.render("Press SPACE to Restart or ESC to Quit", True, WHITE)
    win.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 3))
    win.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Restart game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()