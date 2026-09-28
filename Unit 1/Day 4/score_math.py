# ICD2O Lesson 4: Score Math
# Thursday, September 24
#
# The panel at the top shows the expressions the game is working out
# while you play: the score calculation, the timer, and the wrap.
#
# Change values in EDIT ZONE 1 and expressions in EDIT ZONE 2 only.
# Change ONE thing. Predict what the player will see. Save. Run.
#
# Controls: arrow keys or W A S D. Walk off the right edge and see what
# the wrap does. Collect coins, then reach the door before the timer ends.

import pygame

# ============================================================
# EDIT ZONE 1: STARTING VALUES
# ============================================================
coin_value = 10
combo_step = 1
start_seconds = 45
bonus_base = 2
# ============================================================

pygame.init()
WIDTH = 960
HEIGHT = 600
PANEL_HEIGHT = 210
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Score Math")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)
title_font = pygame.font.SysFont("consolas", 20, bold=True)

FLOOR = (38, 54, 74)
PANEL = (32, 46, 64)
CREAM = (242, 240, 233)
MUTED = (185, 198, 210)
GOLD = (240, 200, 80)
AMBER = (224, 169, 85)
TEAL = (94, 176, 160)
PURPLE = (176, 150, 230)
RED = (232, 120, 104)
DOOR_SHUT = (120, 84, 60)
DOOR_OPEN = (94, 176, 160)

PLAYER_SIZE = 32
start_x = 60.0
start_y = 380.0
player_x = start_x
player_y = start_y
player_speed = 4.0

score = 0
combo = 0
coins_collected = 0
bonus = 0
frames = 0
time_left = start_seconds
last_calc = "no coins yet"
message = "Collect coins, then reach the door."
game_over = False
finished = False

coin_1 = pygame.Rect(250, 280, 20, 20)
coin_2 = pygame.Rect(430, 500, 20, 20)
coin_3 = pygame.Rect(650, 300, 20, 20)
coin_1_taken = False
coin_2_taken = False
coin_3_taken = False
door = pygame.Rect(890, 330, 40, 100)


def draw_line(text, x, y, colour):
    screen.blit(font.render(text, True, colour), (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over and not finished:
        frames = frames + 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x = player_x - player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x = player_x + player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y = player_y - player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y = player_y + player_speed

    # ---- The wrap: % keeps player_x inside 0 to WIDTH ----
    player_x = player_x % WIDTH

    if player_y < PANEL_HEIGHT:
        player_y = float(PANEL_HEIGHT)
    if player_y > HEIGHT - PLAYER_SIZE:
        player_y = float(HEIGHT - PLAYER_SIZE)

    # ---- The timer: // turns frames into whole seconds ----
    time_left = start_seconds - frames // 60
    minutes_part = time_left // 60
    seconds_part = time_left % 60

    player = pygame.Rect(int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE)

    coin_touched = False
    if not coin_1_taken and player.colliderect(coin_1):
        coin_1_taken = True
        coin_touched = True
    if not coin_2_taken and player.colliderect(coin_2):
        coin_2_taken = True
        coin_touched = True
    if not coin_3_taken and player.colliderect(coin_3):
        coin_3_taken = True
        coin_touched = True

    # ============================================================
    # EDIT ZONE 2: THE EXPRESSIONS
    # If you change the score line, change the last_calc line to match.
    # ============================================================
    if coin_touched:
        coins_collected = coins_collected + 1
        combo = combo + combo_step
        old_score = score
        score = score + coin_value * combo ** 2
        last_calc = (str(old_score) + " + " + str(coin_value) + " * "
                     + str(combo) + "  =  " + str(score))
        message = "Coin. The multiply happens before the add."

    if not finished and player.colliderect(door):
        bonus = bonus_base ** coins_collected
        score = score + bonus
        finished = True
        message = ("Door. bonus = " + str(bonus_base) + " ** "
                   + str(coins_collected) + " = " + str(bonus)
                   + ". Final score " + str(score) + ".")
    # ============================================================
    # End of EDIT ZONE 2.
    # ============================================================

    if not finished and time_left < 1:
        game_over = True
        message = "Time is up. Close the window and run it again."

    # ---- Draw ----
    screen.fill(FLOOR)
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, AMBER, (0, PANEL_HEIGHT), (WIDTH, PANEL_HEIGHT), 3)

    draw_line("EXPRESSION PANEL: what the game is working out right now", 24, 12, AMBER)
    draw_line("coins = " + str(coins_collected)
              + "    combo = " + str(combo)
              + "    score = " + str(score), 24, 44, CREAM)
    draw_line("score = score + coin_value * combo", 24, 74, TEAL)
    draw_line("last coin:  " + last_calc, 24, 100, MUTED)
    clock_text = str(minutes_part) + ":" + str(seconds_part)
    if seconds_part < 10:
        clock_text = str(minutes_part) + ":0" + str(seconds_part)
    draw_line("time_left = start_seconds - frames // 60  =  " + str(time_left)
              + "     clock " + clock_text, 24, 130, PURPLE)
    draw_line("player_x % " + str(WIDTH) + "  =  " + str(round(player_x, 1)), 24, 160, GOLD)
    draw_line(str(message), 24, 184, CREAM)

    if not coin_1_taken:
        pygame.draw.circle(screen, GOLD, coin_1.center, 10)
    if not coin_2_taken:
        pygame.draw.circle(screen, GOLD, coin_2.center, 10)
    if not coin_3_taken:
        pygame.draw.circle(screen, GOLD, coin_3.center, 10)

    if finished:
        pygame.draw.rect(screen, DOOR_OPEN, door)
    else:
        pygame.draw.rect(screen, DOOR_SHUT, door)

    pygame.draw.rect(screen, GOLD, player)
    if time_left < 11:
        draw_line("HURRY", 24, 210 + 10, RED)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
