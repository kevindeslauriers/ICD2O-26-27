# ICD2O Lesson 5: Player Setup (challenge)
# Monday, September 28
#
# Everything the game needs is typed by the player before the window opens.
# Run it, answer the three questions in the TERMINAL, then play.
#
# Controls: arrow keys or W A S D. The red block costs you a life.
# Close the window to stop.

import pygame

print("=== PLAYER SETUP ===")
player_name = input("Name your player: ")
player_speed = float(input("How fast should they move (try 2.5, then 9)? "))
lives = int(input("How many lives do they start with? "))
print("Starting the game for", player_name)

pygame.init()
WIDTH = 900
HEIGHT = 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ICD2O Player Setup")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)

FLOOR = (38, 54, 74)
RED = (214, 92, 76)
PANEL = (32, 46, 64)
CREAM = (242, 240, 233)
AMBER = (224, 169, 85)
GOLD = (240, 200, 80)

PLAYER_SIZE = 32
start_x = 60.0
start_y = 300.0
player_x = start_x
player_y = start_y
spike = pygame.Rect(440, 280, 44, 44)
message = "Avoid the red block."
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
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
    if player_y < 175:
        player_y = 175.0
    if player_y > HEIGHT - PLAYER_SIZE:
        player_y = float(HEIGHT - PLAYER_SIZE)

    player = pygame.Rect(int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE)

    if not game_over and player.colliderect(spike):
        lives = lives - 1
        player_x = start_x
        player_y = start_y
        message = "Ouch. That cost a life."

    if not game_over and lives < 1:
        game_over = True
        message = "Out of lives. Close the window and run it again."

    screen.fill(FLOOR)
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, 165))
    pygame.draw.line(screen, AMBER, (0, 165), (WIDTH, 165), 3)
    screen.blit(font.render("YOU TYPED THESE. THE GAME IS USING THEM.", True, AMBER), (24, 14))
    screen.blit(font.render("player_name = " + player_name
                            + "   (" + type(player_name).__name__ + ")", True, CREAM), (24, 46))
    screen.blit(font.render("player_speed = " + str(player_speed)
                            + "   (" + type(player_speed).__name__ + ")"
                            + "    lives = " + str(lives)
                            + "   (" + type(lives).__name__ + ")", True, CREAM), (24, 74))
    screen.blit(font.render(str(message), True, AMBER), (24, 130))

    pygame.draw.rect(screen, RED, spike)
    player = pygame.Rect(int(player_x), int(player_y), PLAYER_SIZE, PLAYER_SIZE)
    pygame.draw.rect(screen, GOLD, player)
    screen.blit(font.render(player_name, True, CREAM), (player.x, player.y - 26))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()