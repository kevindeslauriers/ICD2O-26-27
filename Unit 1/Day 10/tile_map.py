# ICD2O Lesson 9: Tile Map
#
# The whole map is drawn by NESTED LOOPS: the outer loop goes down the
# rows, the inner loop goes across the columns, one tile at a time.
# The coin trail is placed by a WHILE loop.
#
# Look for the line "while running:" further down. It is a while loop
# too: it keeps the game going until you close the window, which sets
# running to False. Every pygame demo you have run uses one.
#
# Change only the EDIT ZONES.
# Change ONE thing. Predict what the player will see. Save (Ctrl+S). Run.
#
# Controls: arrow keys or W A S D. Reach the green goal tile.

import pygame

# ============================================================
# EDIT ZONE 1: MAP SIZE
# Keep cols * tile_size at 1200 or less so the window fits.
# ============================================================
rows = 8
cols = 12
tile_size = 48
goal_row = 6
goal_col = 10
coin_row = 3
coin_gap = 2
# ============================================================
# End of EDIT ZONE 1.
# ============================================================

pygame.init()
PANEL_HEIGHT = 110
WIDTH = cols * tile_size
if WIDTH < 640:
    WIDTH = 640
HEIGHT = PANEL_HEIGHT + rows * tile_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Tile Map")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 20)
title_font = pygame.font.SysFont("consolas", 20, bold=True)

PANEL = (32, 46, 64)
CREAM = (242, 240, 233)
MUTED = (185, 198, 210)
AMBER = (224, 169, 85)
GOLD = (240, 200, 80)
GRASS = (96, 150, 96)
GRASS_DARK = (78, 128, 80)
WALL = (70, 74, 84)
GOAL = (94, 196, 140)
PLAYER_COLOUR = (240, 120, 90)

PLAYER_SIZE = tile_size // 2
player_x = float(tile_size + tile_size // 4)
player_y = float(PANEL_HEIGHT + tile_size + tile_size // 4)
player_speed = 3.0
message = "Reach the green goal tile."

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- Movement (stays inside the outer walls) ----
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x = player_x - player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x = player_x + player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y = player_y - player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y = player_y + player_speed

    if player_x < tile_size:
        player_x = float(tile_size)
    if player_x > (cols - 1) * tile_size - PLAYER_SIZE:
        player_x = float((cols - 1) * tile_size - PLAYER_SIZE)
    if player_y < PANEL_HEIGHT + tile_size:
        player_y = float(PANEL_HEIGHT + tile_size)
    if player_y > PANEL_HEIGHT + (rows - 1) * tile_size - PLAYER_SIZE:
        player_y = float(PANEL_HEIGHT + (rows - 1) * tile_size - PLAYER_SIZE)

    # Which tile is the centre of the player on? // gives whole tiles.
    player_col = int(player_x + PLAYER_SIZE // 2) // tile_size
    player_row = int(player_y - PANEL_HEIGHT + PLAYER_SIZE // 2) // tile_size

    if player_row == goal_row and player_col == goal_col:
        message = "You reached the goal!"

    screen.fill(PANEL)

    # ============================================================
    # EDIT ZONE 2: DRAW THE MAP WITH NESTED LOOPS
    # The inner loop runs all the way across for EACH row.
    # The pygame.draw.rect line draws one tile. Leave that line as it is.
    # ============================================================
    tiles_drawn = 0
    for row in range(rows):
        for col in range(cols):
            tile_colour = GRASS
            if (row + col) % 2 == 0:
                tile_colour = GRASS_DARK
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                tile_colour = WALL
            if row == goal_row and col == goal_col:
                tile_colour = GOAL
            pygame.draw.rect(screen, tile_colour, (col * tile_size, PANEL_HEIGHT + row * tile_size, tile_size - 2, tile_size - 2))
            tiles_drawn = tiles_drawn + 1
    # ============================================================
    # End of EDIT ZONE 2.
    # ============================================================

    # ============================================================
    # EDIT ZONE 3: THE COIN TRAIL WITH A WHILE LOOP
    # Start at column 1 and jump coin_gap columns each pass,
    # until the next column would be in the right wall.
    # WARNING: if coin_gap is 0, coin_col never changes and the loop
    # never ends. The window freezes. Close it from the terminal with Ctrl+C.
    # ============================================================
    coins_drawn = 0
    coin_col = 1
    while coin_col < cols - 1:
        coin_x = coin_col * tile_size + tile_size // 2
        coin_y = PANEL_HEIGHT + coin_row * tile_size + tile_size // 2
        pygame.draw.circle(screen, GOLD, (coin_x, coin_y), tile_size // 6)
        coins_drawn = coins_drawn + 1
        coin_col = coin_col + coin_gap
    # ============================================================
    # End of EDIT ZONE 3.
    # ============================================================

    pygame.draw.rect(screen, PLAYER_COLOUR, (int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE))

    # ---- Panel ----
    pygame.draw.line(screen, AMBER, (0, PANEL_HEIGHT - 4), (WIDTH, PANEL_HEIGHT - 4), 3)
    screen.blit(title_font.render("TILE MAP", True, AMBER), (16, 10))
    screen.blit(font.render("rows = " + str(rows) + "   cols = " + str(cols) + "   tiles_drawn = " + str(tiles_drawn), True, CREAM), (16, 36))
    screen.blit(font.render("coins_drawn = " + str(coins_drawn) + "   player on row " + str(player_row) + ", col " + str(player_col), True, CREAM), (16, 60))
    screen.blit(font.render(message, True, MUTED), (16, 84))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
