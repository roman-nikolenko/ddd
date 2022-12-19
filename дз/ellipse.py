import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
w = 25
num = int(input())

pygame.init()

win = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Bruh')
win.fill(BLACK)

for x in range(num):
    for y in range(num):
            pygame.draw.ellipse(win, (WHITE), (300 // 2, 0, w * x, 300), 1)
            pygame.draw.ellipse(win, (WHITE), (300 // 2, 0, w * y, 300), 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()

