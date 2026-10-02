# ICD2O Lesson 7: Vault Door
# Friday, October 2
#
# The door now needs TWO things. The spike only hurts if you have
# no shield. Both rules are conditions built with and, or, not.
#
# The panel at the top shows each rule as True or False, live.
#
# Change only EDIT ZONE 1 and EDIT ZONE 2.
# Change ONE thing. Predict what the player will see. Save (Ctrl+S). Run.
#
# Controls: arrow keys or W A S D.
# Coins are gold. The key is amber. The shield is blue.
# The spike is red. The door is on the right.

import pygame

# ============================================================
# EDIT ZONE 1: STARTING VALUES
# ============================================================
score = 0
lives = 3
has_key = False
has_shield = False
score_needed = 30
# ============================================================
# End of EDIT ZONE 1.
# ============================================================

pygame.init()
WIDTH = 960
HEIGHT = 600
PANEL_HEIGHT = 170
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Vault Door")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)
title_font = pygame.font.SysFont("consolas", 20, bold=True)

PANEL = (32, 46, 64)
FLOOR = (38, 54, 74)
CREAM = (242, 240, 233)
MUTED = (185, 198, 210)
GOLD = (240, 200, 80)
AMBER = (224, 169, 85)
BLUE = (110, 160, 230)
RED = (214, 92, 76)
TEAL = (94, 176, 160)
DOOR_SHUT = (120, 84, 60)
DOOR_OPEN = (94, 176, 160)

PLAYER_SIZE = 32
start_x = 60.0
start_y = 460.0
player_x = start_x
player_y = start_y
player_speed = 4.0

coin_value = 10
coin_1 = pygame.Rect(220, 260, 20, 20)
coin_2 = pygame.Rect(400, 500, 20, 20)
coin_3 = pygame.Rect(560, 260, 20, 20)
coin_1_taken = False
coin_2_taken = False
coin_3_taken = False

key_rect = pygame.Rect(700, 520, 24, 24)
key_taken = False
shield_rect = pygame.Rect(130, 520, 24, 24)
shield_taken = False
spike = pygame.Rect(480, 360, 44, 44)
door = pygame.Rect(890, 330, 40, 100)

door_open = False
game_over = False
message = "The door needs the key and a score of " + str(score_needed) + "."

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- Movement ----
    if not game_over and not door_open:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x = player_x - player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x = player_x + player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y = player_y - player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y = player_y + player_speed

    if player_x < 0:
        player_x = 0.0
    if player_x > WIDTH - PLAYER_SIZE:
        player_x = float(WIDTH - PLAYER_SIZE)
    if player_y < PANEL_HEIGHT:
        player_y = float(PANEL_HEIGHT)
    if player_y > HEIGHT - PLAYER_SIZE:
        player_y = float(HEIGHT - PLAYER_SIZE)

    player = pygame.Rect(int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE)

    # ---- Pick things up ----
    if not coin_1_taken and player.colliderect(coin_1):
        coin_1_taken = True
        score = score + coin_value
        message = "Coin collected."
    if not coin_2_taken and player.colliderect(coin_2):
        coin_2_taken = True
        score = score + coin_value
        message = "Coin collected."
    if not coin_3_taken and player.colliderect(coin_3):
        coin_3_taken = True
        score = score + coin_value
        message = "Coin collected."
    if not key_taken and player.colliderect(key_rect):
        key_taken = True
        has_key = True
        message = "You picked up the key."
    if not shield_taken and player.colliderect(shield_rect):
        shield_taken = True
        has_shield = True
        message = "You picked up the shield."

    touching_spike = player.colliderect(spike)
    touching_door = player.colliderect(door)
    send_back = False

    # ============================================================
    # EDIT ZONE 2: THE RULES
    # Each rule is a condition. Python works it out and stores
    # True or False. The panel shows both rules live.
    # ============================================================
    door_can_open = has_key and score >= score_needed
    spike_hurts = not has_shield

    if touching_door and not door_open:
        if door_can_open:
            door_open = True
            message = "The door opens. You escape!"
        elif has_key:
            message = "You have the key, but you need a score of " + str(score_needed) + "."
        else:
            message = "Locked. You need the key."

    if touching_spike and not game_over:
        if spike_hurts:
            lives = lives - 1
            send_back = True
            message = "Ouch. Back to the start."
        else:
            message = "The spike does not hurt you."
    # ============================================================
    # End of EDIT ZONE 2.
    # ============================================================

    if send_back:
        player_x = start_x
        player_y = start_y
    if touching_door and not door_open:
        player_x = float(door.x - PLAYER_SIZE - 6)

    if not game_over and lives < 1:
        game_over = True
        message = "Out of lives. Close the window and run it again."

    # ---- Draw ----
    screen.fill(FLOOR)

    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, AMBER, (0, PANEL_HEIGHT), (WIDTH, PANEL_HEIGHT), 3)
    heading = title_font.render("VALUES", True, AMBER)
    screen.blit(heading, (24, 12))
    heading = title_font.render("RULES (True or False, right now)", True, AMBER)
    screen.blit(heading, (420, 12))

    screen.blit(font.render("score = " + str(score), True, CREAM), (24, 42))
    screen.blit(font.render("lives = " + str(lives), True, CREAM), (24, 70))
    screen.blit(font.render("has_key = " + str(has_key), True, CREAM), (24, 98))
    screen.blit(font.render("has_shield = " + str(has_shield), True, CREAM), (220, 42))
    screen.blit(font.render("score_needed = " + str(score_needed), True, CREAM), (220, 70))

    rule_colour = RED
    if door_can_open:
        rule_colour = TEAL
    screen.blit(font.render("door_can_open = " + str(door_can_open), True, rule_colour), (420, 42))
    rule_colour = RED
    if spike_hurts:
        rule_colour = TEAL
    screen.blit(font.render("spike_hurts = " + str(spike_hurts), True, rule_colour), (420, 70))

    screen.blit(font.render(str(message), True, MUTED), (24, 134))

    if not coin_1_taken:
        pygame.draw.circle(screen, GOLD, coin_1.center, 10)
    if not coin_2_taken:
        pygame.draw.circle(screen, GOLD, coin_2.center, 10)
    if not coin_3_taken:
        pygame.draw.circle(screen, GOLD, coin_3.center, 10)
    if not key_taken:
        pygame.draw.rect(screen, AMBER, key_rect, border_radius=4)
    if not shield_taken:
        pygame.draw.rect(screen, BLUE, shield_rect, border_radius=12)
    pygame.draw.rect(screen, RED, spike)

    if door_open:
        pygame.draw.rect(screen, DOOR_OPEN, door)
    else:
        pygame.draw.rect(screen, DOOR_SHUT, door)

    pygame.draw.rect(screen, GOLD, player)
    if has_shield:
        pygame.draw.rect(screen, BLUE, player, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
