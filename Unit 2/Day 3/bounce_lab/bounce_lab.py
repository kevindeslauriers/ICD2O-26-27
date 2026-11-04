# Bounce Lab: ICD2O studio challenge
# Role A (Movement), Role B (Rules), Role C (Detector)
# Only change code inside YOUR edit zone.
# Run bounce_check.py to test your functions.
# Run this file to play the game.

import pygame

# ---------- Settings ----------
WIDTH = 800
HEIGHT = 600
BOX_SIZE = 60
MAX_SPEED = 12

# ---------- Colours ----------
WHITE = (255, 255, 255)
RED = (230, 60, 60)
YELLOW = (240, 220, 60)
GREEN = (60, 200, 90)
BLUE = (60, 120, 230)
GREY = (160, 160, 170)
DARK = (25, 25, 40)
FLASH = (120, 30, 70)


# =====================================================
# EDIT ZONE A: Movement (Role A)
# =====================================================
def check_wall(position, speed, edge):
    # position: the left side of the box (for x) or the top of the box (for y)
    # speed: how far the box moves each frame. Negative means left or up.
    # edge: the width or the height of the window
    # The box is BOX_SIZE pixels wide and tall.
    # Return the speed the box should have next frame.
    # Right now the box never turns around, so it flies off the screen.
    return speed


# =====================================================
# EDIT ZONE B: Rules (Role B)
# =====================================================
def pick_colour(bounces):
    # bounces: how many times box 1 has hit a wall so far
    # Return the colour box 1 should be.
    return WHITE


def boost_speed(speed, bounces):
    # The engine calls this once, every time box 1 bounces.
    # speed: box 1's speed right after the bounce
    # bounces: the bounce count, including this bounce
    # Return box 1's new speed.
    return speed


# =====================================================
# EDIT ZONE C: Detector (Role C)
# =====================================================
def is_touching(x1, y1, x2, y2):
    # (x1, y1) is the top left corner of box 1.
    # (x2, y2) is the top left corner of box 2.
    # Both boxes are BOX_SIZE pixels wide and tall.
    # Return True when the boxes overlap, False when they do not.
    return False


def background_colour(touching):
    # touching: True or False
    # Return the colour of the background.
    return DARK


# =====================================================
# STUDIO ENGINE: do not change anything below this line
# =====================================================
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    box1_x = 100
    box1_y = 150
    box1_speed_x = 4
    box1_speed_y = 3

    box2_x = 500
    box2_y = 350
    box2_speed_x = -3
    box2_speed_y = 2

    bounces = 0
    touches = 0
    was_touching = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move both boxes
        box1_x = box1_x + box1_speed_x
        box1_y = box1_y + box1_speed_y
        box2_x = box2_x + box2_speed_x
        box2_y = box2_y + box2_speed_y

        # Box 1 walls (Role A), bounce count and boost (Role B)
        new_speed = check_wall(box1_x, box1_speed_x, WIDTH)
        if new_speed != box1_speed_x:
            bounces = bounces + 1
            new_speed = boost_speed(new_speed, bounces)
        box1_speed_x = new_speed

        new_speed = check_wall(box1_y, box1_speed_y, HEIGHT)
        if new_speed != box1_speed_y:
            bounces = bounces + 1
            new_speed = boost_speed(new_speed, bounces)
        box1_speed_y = new_speed

        # Box 2 walls (Role A)
        box2_speed_x = check_wall(box2_x, box2_speed_x, WIDTH)
        box2_speed_y = check_wall(box2_y, box2_speed_y, HEIGHT)

        # Touching (Role C)
        touching = is_touching(box1_x, box1_y, box2_x, box2_y)
        if touching and not was_touching:
            touches = touches + 1
        was_touching = touching

        # Draw
        screen.fill(background_colour(touching))
        pygame.draw.rect(screen, pick_colour(bounces), (box1_x, box1_y, BOX_SIZE, BOX_SIZE))
        pygame.draw.rect(screen, GREY, (box2_x, box2_y, BOX_SIZE, BOX_SIZE))
        pygame.display.set_caption("Bounce Lab    Bounces: " + str(bounces) + "    Touches: " + str(touches))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run_game()
