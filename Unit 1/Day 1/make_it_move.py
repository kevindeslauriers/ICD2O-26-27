# ICD2O Day 1: Make It Move
# Kevin DesLauriers, Bayview Glen
# This is the finished version of what we build together in class.
# Type it yourself. Do not paste it.

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ICD2O Studio: Day 1")
clock = pygame.time.Clock()

player_x = 100
player_y = 300
player_size = 40
player_speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x = player_x + player_speed
    if keys[pygame.K_LEFT]:
        player_x = player_x - player_speed
    if keys[pygame.K_UP]:
        player_y = player_y - player_speed
    if keys[pygame.K_DOWN]:
        player_y = player_y + player_speed

    screen.fill((20, 20, 40))
    player_box = (player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, (255, 200, 0), player_box)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
