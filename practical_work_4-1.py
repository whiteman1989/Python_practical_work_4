import pygame
from pygame import display
from pygame import key

n = 1 # number in group

display_size = 500+n+n*10

pygame.init()
win = pygame.display.set_mode((display_size, display_size))

pygame.display.set_caption("Practical_work_4")

x= 50
y = 425
width = n+n*10
heigth = 60
speed = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < display_size - width - 5:
        x += speed
    if not (isJump):
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < display_size - heigth -5:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount**2)/2
            else:
                y -= (jumpCount**2)/2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y , width, heigth))
    pygame.display.update()

pygame.quit()