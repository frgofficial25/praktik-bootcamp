import pygame
import sys

# init
pygame.init()

# membuat display surface object
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

while True :
    # user input, database input
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < 500 - panjang:
        x += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    if keys[pygame.K_DOWN] and y < 500 - lebar:
        y += speed

    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,120,0), (x, y, lebar, panjang))
    # render ke display
    pygame.display.flip()
    clock.tick(60)