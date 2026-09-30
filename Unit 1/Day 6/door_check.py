# ICD2O Lesson 6: Door Check (challenge)
# Wednesday, September 30
#
# In Lesson 3 the door opened whenever has_key held anything at all.
# Now the game actually checks, and there is a rank message that uses elif.
#
# Change only EDIT ZONE 1 and EDIT ZONE 2.
# Controls: arrow keys or W A S D. Collect coins, take the key, reach the door.

import pygame

# ============================================================
# EDIT ZONE 1: STARTING VALUES
# ============================================================
coin_value = 10
locked_message = "Locked. You need the key."
open_message = "The door opens."
# ============================================================

pygame.init()
WIDTH = 960
HEIGHT = 600
PANEL_HEIGHT = 150
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Door Check")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)

FLOOR = (38, 54, 74)
PANEL = (32, 46, 64)
CREAM = (242, 240, 233)
MUTED = (185, 198, 210)
GOLD = (240, 200, 80)
AMBER = (224, 169, 85)
TEAL = (94, 176, 160)
DOOR_SHUT = (120, 84, 60)
DOOR_OPEN = (94, 176, 160)

PLAYER_SIZE = 32
player_x = 60.0
player_y = 400.0
player_speed = 4.0

score = 0
has_key = False
rank = "No rank yet"
message = "Find the key, then the door."
finished = False

coin_1 = pygame.Rect(260, 300, 20, 20)
coin_2 = pygame.Rect(430, 500, 20, 20)
coin_3 = pygame.Rect(610, 280, 20, 20)
coin_1_taken = False
coin_2_taken = False
coin_3_taken = False
key_rect = pygame.Rect(740, 480, 24, 24)
key_taken = False
door = pygame.Rect(890, 330, 40, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not finished:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x = player_x - player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x = player_x + player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y = player_y - player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y = player_y + player_speed

    player_x = player_x % WIDTH
    if player_y < PANEL_HEIGHT:
        player_y = float(PANEL_HEIGHT)
    if player_y > HEIGHT - PLAYER_SIZE:
        player_y = float(HEIGHT - PLAYER_SIZE)

    player = pygame.Rect(int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE)

    if not coin_1_taken and player.colliderect(coin_1):
        coin_1_taken = True
        score = score + coin_value
    if not coin_2_taken and player.colliderect(coin_2):
        coin_2_taken = True
        score = score + coin_value
    if not coin_3_taken and player.colliderect(coin_3):
        coin_3_taken = True
        score = score + coin_value

    if not key_taken and player.colliderect(key_rect):
        key_taken = True
        has_key = True
        message = "You have the key."

    # ============================================================
    # EDIT ZONE 2: THE DECISIONS
    # ============================================================
    if score >= 30:
        rank = "Gold"
    elif score >= 20:
        rank = "Silver"
    elif score >= 10:
        rank = "Bronze"
    else:
        rank = "No rank yet"

    if not finished and player.colliderect(door):
        if has_key:
            finished = True
            message = open_message
        else:
            message = locked_message
            player_x = float(door.x - PLAYER_SIZE - 6)
    # ============================================================
    # End of EDIT ZONE 2.
    # ============================================================

    screen.fill(FLOOR)
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, AMBER, (0, PANEL_HEIGHT), (WIDTH, PANEL_HEIGHT), 3)
    screen.blit(font.render("THE GAME IS DECIDING, EVERY FRAME", True, AMBER), (24, 14))
    screen.blit(font.render("score = " + str(score)
                            + "      has_key = " + str(has_key), True, CREAM), (24, 48))
    screen.blit(font.render("rank = " + rank, True, TEAL), (24, 80))
    screen.blit(font.render(str(message), True, MUTED), (24, 112))

    if not coin_1_taken:
        pygame.draw.circle(screen, GOLD, coin_1.center, 10)
    if not coin_2_taken:
        pygame.draw.circle(screen, GOLD, coin_2.center, 10)
    if not coin_3_taken:
        pygame.draw.circle(screen, GOLD, coin_3.center, 10)
    if not key_taken:
        pygame.draw.rect(screen, AMBER, key_rect, border_radius=4)

    if finished:
        pygame.draw.rect(screen, DOOR_OPEN, door)
    else:
        pygame.draw.rect(screen, DOOR_SHUT, door)

    pygame.draw.rect(screen, GOLD, player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
