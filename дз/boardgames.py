import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

a,n = input().split()

a = int(a)
n = int(n)

size = a//n

pygame.init()

win = pygame.display.set_mode((a, a))
pygame.display.set_caption('квадраты')
win.fill((0, 225, 0))

for x in range(n):
    for y in range(n):
        if (x + y) % 2 == 0:
            pygame.draw.rect(win, (WHITE), [size * x, size * y, size, size])
        else:
            pygame.draw.rect(win, (BLACK), [size * x, size * y, size, size])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()