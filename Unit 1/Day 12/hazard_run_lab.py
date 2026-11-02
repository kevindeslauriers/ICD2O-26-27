# ICD2O Lesson 10 Lab: Hazard Run
# SPACE: step onto the next tile.  S: shield on or off.  UP: level up.  R: restart.
# Close the window to quit.
# You only edit the two EDIT ZONES. Change one thing, predict, save, run.
# The teacher code below CALLS your three functions. The panel shows every call
# and the value your function gave back.

import pygame

# ==================== EDIT ZONE 1: starting values ====================
start_lives = 10        # lives at the start of the run
start_level = 1         # level at the start (UP adds 1)
start_shield = False    # True or False. S switches it while you play.
# ==================== END OF EDIT ZONE 1 ==============================


# ==================== EDIT ZONE 2: your functions ====================
def damage_after_shield(hit, has_shield):
    # TASK 2: with a shield, the player only takes half the hit (use //).
    return hit


def coin_value(level):
    # TASK 3: a coin should be worth 10 points times the level.
    return 10


def rank_for(score):
    # TASK 4: this is the door check order bug from Lesson 6. Fix it.
    if score >= 50:
        return "Bronze"
    elif score >= 150:
        return "Gold"
    elif score >= 100:
        return "Silver"
    else:
        return "No rank yet"
# ==================== END OF EDIT ZONE 2 =============================


# ----- Teacher code: read it if you like, but do not change it. -----
pygame.init()
WIDTH = 1100
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Hazard Run Lab")
clock = pygame.time.Clock()
big_font = pygame.font.SysFont("consolas", 34)
font = pygame.font.SysFont("consolas", 24)
small_font = pygame.font.SysFont("consolas", 20)

BACKGROUND = (20, 32, 46)
PANEL = (34, 50, 74)
CREAM = (242, 240, 233)
MUTED = (185, 198, 210)
AMBER = (224, 169, 85)
TEAL = (94, 176, 160)
RED = (232, 120, 104)
COIN = (240, 200, 80)
FLOOR = (60, 80, 104)
SHIELD = (120, 180, 240)

SPIKE_HIT = 2
LAVA_HIT = 5
TILES = ["coin", "spike", "coin", "lava", "coin", "coin", "spike", "coin", "lava", "goal"]
TILE_SIZE = 90
GAP = 8
LEFT = 60
TOP = 150

lives = start_lives
level = start_level
has_shield = start_shield
score = 0
step = -1
message = "Press SPACE to step onto the first tile."
last_call = "No function called yet."
game_over = False
running = True


def draw_text(text, x, y, colour, which_font):
    screen.blit(which_font.render(text, True, colour), (x, y))


def draw_tile(index, kind):
    x = LEFT + index * (TILE_SIZE + GAP)
    pygame.draw.rect(screen, FLOOR, (x, TOP, TILE_SIZE, TILE_SIZE), border_radius=10)
    centre_x = x + TILE_SIZE // 2
    centre_y = TOP + TILE_SIZE // 2
    if kind == "coin":
        pygame.draw.circle(screen, COIN, (centre_x, centre_y), 20)
    elif kind == "spike":
        pygame.draw.polygon(screen, MUTED, [(centre_x - 25, centre_y + 22), (centre_x, centre_y - 24), (centre_x + 25, centre_y + 22)])
    elif kind == "lava":
        pygame.draw.rect(screen, RED, (x + 12, centre_y - 14, TILE_SIZE - 24, 28), border_radius=8)
    elif kind == "goal":
        pygame.draw.rect(screen, TEAL, (x + 18, TOP + 18, TILE_SIZE - 36, TILE_SIZE - 36), border_radius=6)
# ----- End of teacher setup -----

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                has_shield = not has_shield
            if event.key == pygame.K_UP:
                level = level + 1
            if event.key == pygame.K_r:
                lives = start_lives
                level = start_level
                has_shield = start_shield
                score = 0
                step = -1
                game_over = False
                message = "Restarted. Press SPACE."
                last_call = "No function called yet."
            if event.key == pygame.K_SPACE and not game_over and step < len(TILES) - 1:
                step = step + 1
                kind = TILES[step]
                if kind == "coin":
                    value = coin_value(level)
                    last_call = "coin_value(" + str(level) + ") gave back " + str(value)
                    score = score + value
                    message = "Coin!"
                elif kind == "spike" or kind == "lava":
                    hit = SPIKE_HIT
                    if kind == "lava":
                        hit = LAVA_HIT
                    damage = damage_after_shield(hit, has_shield)
                    last_call = "damage_after_shield(" + str(hit) + ", " + str(has_shield) + ") gave back " + str(damage)
                    lives = lives - damage
                    message = "Ouch: " + kind
                    if lives <= 0:
                        game_over = True
                        message = "Game over on tile " + str(step + 1) + ". Press R."
                elif kind == "goal":
                    rank = rank_for(score)
                    last_call = "rank_for(" + str(score) + ") gave back " + str(rank)
                    message = "Goal! Rank: " + str(rank) + ". Press R."

    # ----- Teacher code: drawing -----
    screen.fill(BACKGROUND)
    draw_text("Hazard Run Lab", LEFT, 40, CREAM, big_font)
    draw_text("SPACE step   S shield   UP level   R restart", LEFT, 90, MUTED, small_font)

    for index in range(len(TILES)):
        draw_tile(index, TILES[index])
    if step >= 0:
        player_x = LEFT + step * (TILE_SIZE + GAP) + TILE_SIZE // 2
    else:
        player_x = LEFT - 30
    player_colour = CREAM
    if has_shield:
        pygame.draw.circle(screen, SHIELD, (player_x, TOP + TILE_SIZE + 40), 26, 4)
    pygame.draw.circle(screen, player_colour, (player_x, TOP + TILE_SIZE + 40), 18)

    pygame.draw.rect(screen, PANEL, (LEFT, 330, WIDTH - 2 * LEFT, 250), border_radius=16)
    draw_text("lives      = " + str(lives), LEFT + 30, 350, AMBER, big_font)
    draw_text("score      = " + str(score), LEFT + 30, 395, TEAL, big_font)
    draw_text("level      = " + str(level), LEFT + 30, 445, MUTED, font)
    draw_text("has_shield = " + str(has_shield), LEFT + 30, 480, MUTED, font)
    draw_text("last call: " + last_call, LEFT + 30, 525, CREAM, font)
    draw_text("message: " + message, LEFT + 500, 360, CREAM, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
