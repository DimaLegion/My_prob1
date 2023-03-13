# Продолжить разработку игры. Доработать еду для змейки (змейка увеличивается при поедании чего-нибудь)
# По желанию добавить:
# -Фон
# -Счётчик очков

import pygame, random

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
icon = pygame.image.load("snake.png").convert()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
length = 1
game_over = False
x1 = random.randrange(100, 600, 50)
y1 = random.randrange(50, 550, 50)
snake = [(x1, y1)]

x1_change = 0
y1_change = 0

x2 = random.randrange(100, 600, 50)
y2 = random.randrange(50, 550, 50)
apple = [(x2, y2)]

clock = pygame.time.Clock()

while not game_over:
    dis.blit(icon, (100, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -50
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 50
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -50
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 50

    x1 += x1_change
    y1 += y1_change
    head = [x1, y1]
    snake.append(head)
    if len(snake) > length:
        del snake[0]
    pygame.draw.rect(dis, red, [x2, y2, 50, 50])
    pygame.draw.rect(dis, blue, [x1, y1, 50, 50])

    if x1 >= 700 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    if x1 == x2 and y1 == y2:
        x2 = random.randrange(100, 600, 50)
        y2 = random.randrange(50, 550, 50)
        length += 1

    for spisok in snake:
        pygame.draw.rect(dis, blue, [spisok[0], spisok[1], 50, 50])

    pygame.display.update()
    clock.tick(2)
pygame = quit()
quit()
