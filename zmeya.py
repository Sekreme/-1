import pygame as pygame
from random import randint

pygame.init()
# Задаем дисплей
side = 30
w = 17
h = 15
sc = pygame.display.set_mode((w * side, h * side))
# Задаем цвета 
K_BLUE = (21, 32, 229)
WHITE = (255, 255, 255) 
YELLOW = (255, 193, 6)

game_running = 0

dirs = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
direction = 0


def place_apple():
    a = (randint(0, w - 1), randint(0, h - 1))
    while a in snake:
        a = (randint(0, w - 1), randint(0, h - 1))
    return a


apple = place_apple()


def check_collisions():
    head = snake[-1]
    for i in range(len(snake) - 1):
        if head == snake[i]:
            return 2
    if head[0] >= w or head[0] < 0:
        return 3
    if head[1] >= h or head[1] < 0:
        return 3
    if head == apple:
        return 1
    return 0


clock = pygame.time.Clock()
f = pygame.font.SysFont('Avenir Heavy', 50, True)

while True:
        clock.tick(4)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                break
            if e.type == pygame.KEYDOWN:
                if game_running == 0:
                    game_runnig = 1
                if e.key == pygame.K_SPACE:
                    game_running = 0
                    snake = [(7, 3), (7, 4)]
                    direction = 0
                    apple = place_apple()
                    
                for i in range(4):
                    if e.key == dirs[i] and direction != (i + 2) % 4:
                        direction = i
                    
                    
    
        x = snake[-1][0] + dx[direction]
        y = snake[-1][1] + dy[direction]
    
        snake.append((x,y))
        coll = check_collisions()
        if coll >= 2:
            game_running = 2
            sc.fill(K_BLUE)
        elif coll == 1:
            apple = place_apple()
        elif coll == 0:
            snake.pop(0)
        
        sc.fill(K_BLUE)
        for i in range(len(snake)):
            pygame.draw.rect(sc,WHITE,(snake[i][0]*side, snake[i][1]*side, side,side))
        pygame.draw.rect(sc, YELLOW, (apple[0]*side, apple[1]*side, side, side))
        pygame.display.update()
                    
pygame.quit()               
                