# ICD2O Lesson 3: Stat Panel
# Tuesday, September 22
#
# The panel at the top of the window shows every variable the game is
# holding right now: its name, its value, and its type.
#
# Your job today: change values in EDIT ZONE 1 and EDIT ZONE 2 only.
# Change ONE thing. Predict what the player will see. Save (Ctrl+S). Run.
#
# Controls: arrow keys or W A S D.
# Coins are gold. The key is amber. The spike is red. The door is on the right.

import pygame

# ============================================================
# EDIT ZONE 1: STARTING VALUES
# ============================================================
player_name = "Nova"
score = 0
lives = 3
player_speed = 4.0
has_key = False
coin_value = 10
message = "Find the key. Then find the door."
# ============================================================
# End of EDIT ZONE 1. Read below if you are curious, but do not
# change anything until you reach EDIT ZONE 2.
# ============================================================

pygame.init()
WIDTH = 960
HEIGHT = 600
PANEL_HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Stat Panel")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)
title_font = pygame.font.SysFont("consolas", 20, bold=True)

NAVY = (20, 32, 46)
PANEL = (32, 46, 64)
FLOOR = (38, 54, 74)
CREAM = (242, 240, 233)
MUTED = (185, 198, 210)
GOLD = (240, 200, 80)
AMBER = (224, 169, 85)
RED = (214, 92, 76)
DOOR_SHUT = (120, 84, 60)
DOOR_OPEN = (94, 176, 160)

# One colour per type, the same colours as the slides.
INT_COLOUR = (94, 176, 160)
FLOAT_COLOUR = (224, 169, 85)
STR_COLOUR = (176, 150, 230)
BOOL_COLOUR = (232, 120, 104)

PLAYER_SIZE = 32
start_x = 70.0
start_y = 380.0
player_x = start_x
player_y = start_y

coin_1 = pygame.Rect(250, 260, 20, 20)
coin_2 = pygame.Rect(400, 500, 20, 20)
coin_3 = pygame.Rect(620, 250, 20, 20)
coin_1_taken = False
coin_2_taken = False
coin_3_taken = False

key_rect = pygame.Rect(720, 510, 24, 24)
key_taken = False
spike = pygame.Rect(480, 340, 44, 44)
door = pygame.Rect(890, 330, 40, 100)
door_open = False
game_over = False


def draw_stat(name, value, x, y):
    # Show a value the way you would type it: text gets quote marks.
    type_name = type(value).__name__
    if type_name == "str":
        shown = '"' + value + '"'
    elif type_name == "float":
        shown = str(round(value, 2))
    else:
        shown = str(value)
    line = font.render(name + " = " + shown, True, CREAM)
    screen.blit(line, (x, y))
    colour = MUTED
    if type_name == "int":
        colour = INT_COLOUR
    elif type_name == "float":
        colour = FLOAT_COLOUR
    elif type_name == "str":
        colour = STR_COLOUR
    elif type_name == "bool":
        colour = BOOL_COLOUR
    badge = font.render(type_name, True, colour)
    screen.blit(badge, (x + 380, y))


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

    # Keep the player on the floor, below the panel.
    if player_x < 0:
        player_x = 0.0
    if player_x > WIDTH - PLAYER_SIZE:
        player_x = float(WIDTH - PLAYER_SIZE)
    if player_y < PANEL_HEIGHT:
        player_y = float(PANEL_HEIGHT)
    if player_y > HEIGHT - PLAYER_SIZE:
        player_y = float(HEIGHT - PLAYER_SIZE)

    player = pygame.Rect(int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE)

    # ---- What did the player touch this frame? ----
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

    spike_touched = False
    if not game_over and player.colliderect(spike):
        spike_touched = True

    # ============================================================
    # EDIT ZONE 2: WHAT HAPPENS WHEN THINGS ARE TOUCHED
    # ============================================================
    if coin_touched:
        score = score + coin_value
        message = "Coin collected."

    if spike_touched:
        lives = lives - 1
        player_x = start_x
        player_y = start_y
        message = "Ouch. Back to the start."
    # ============================================================
    # End of EDIT ZONE 2.
    # ============================================================

    if not key_taken and player.colliderect(key_rect):
        key_taken = True
        has_key = True
        message = "You picked up the key."

    if not door_open and player.colliderect(door):
        if has_key:
            door_open = True
            message = "The door opens. " + player_name + " escapes!"
        else:
            message = "Locked. You need the key."
            player_x = float(door.x - PLAYER_SIZE - 6)

    if spike_touched and lives < 1:
        game_over = True
        message = "Out of lives. Close the window and run it again."

    # ---- Draw ----
    screen.fill(FLOOR)

    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, AMBER, (0, PANEL_HEIGHT), (WIDTH, PANEL_HEIGHT), 3)
    heading = title_font.render("STAT PANEL: every value the game is holding right now", True, AMBER)
    screen.blit(heading, (24, 12))
    draw_stat("player_name", player_name, 24, 44)
    draw_stat("score", score, 24, 74)
    draw_stat("lives", lives, 24, 104)
    draw_stat("has_key", has_key, 24, 134)
    draw_stat("player_speed", player_speed, 500, 44)
    draw_stat("coin_value", coin_value, 500, 74)
    draw_stat("player_x", player_x, 500, 104)
    draw_stat("player_y", player_y, 500, 134)
    note = font.render(str(message), True, MUTED)
    screen.blit(note, (24, 168))

    if not coin_1_taken:
        pygame.draw.circle(screen, GOLD, coin_1.center, 10)
    if not coin_2_taken:
        pygame.draw.circle(screen, GOLD, coin_2.center, 10)
    if not coin_3_taken:
        pygame.draw.circle(screen, GOLD, coin_3.center, 10)
    if not key_taken:
        pygame.draw.rect(screen, AMBER, key_rect, border_radius=4)
    pygame.draw.rect(screen, RED, spike)

    if door_open:
        pygame.draw.rect(screen, DOOR_OPEN, door)
    else:
        pygame.draw.rect(screen, DOOR_SHUT, door)

    pygame.draw.rect(screen, GOLD, player)
    label = font.render(str(player_name), True, CREAM)
    screen.blit(label, (player.x, player.y - 26))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
