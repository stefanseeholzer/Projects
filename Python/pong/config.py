import pygame

pygame.init()
pygame.font.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
BALL_SPEEDUP_INTERVAL = 2500  # milliseconds
BALL_SPEEDUP_FACTOR = 1.05  # 5% faster every interval

# Fonts
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
TITLE_FONT = pygame.font.SysFont("comicsans", 80)
INFO_FONT = pygame.font.SysFont("comicsans", 36)

WIN_SCORE = 10