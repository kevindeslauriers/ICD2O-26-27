# Bounce Lab self check
# Keep this file in the same folder as bounce_lab.py and run it.
# Every line should say PASS. A FAIL tells you what the player would see go wrong.
# Do not change this file.

from bounce_lab import *

passed = 0
total = 0


def check(label, expected, actual):
    global passed, total
    total = total + 1
    if expected == actual:
        passed = passed + 1
        print("  PASS  " + label)
    else:
        print("  FAIL  " + label + "    expected " + str(expected) + ", got " + str(actual))


print("")
print("ROLE A: Movement    check_wall()")
check("box in the middle keeps going right", 4, check_wall(300, 4, WIDTH))
check("box in the middle keeps going left", -4, check_wall(300, -4, WIDTH))
check("box past the left wall turns right", 4, check_wall(-2, -4, WIDTH))
check("box past the right wall turns left", -4, check_wall(745, 4, WIDTH))
check("box past the top turns down", 3, check_wall(-1, -3, HEIGHT))
check("box past the bottom turns up", -3, check_wall(545, 3, HEIGHT))
check("box already heading back from the left wall is not flipped again", 4, check_wall(-5, 4, WIDTH))
check("box already heading back from the right wall is not flipped again", -4, check_wall(760, -4, WIDTH))
check("works for a different window size (edge 400)", -5, check_wall(350, 5, 400))

print("")
print("ROLE B: Rules    pick_colour()")
check("0 bounces is RED", RED, pick_colour(0))
check("1 bounce is YELLOW", YELLOW, pick_colour(1))
check("2 bounces is GREEN", GREEN, pick_colour(2))
check("3 bounces is BLUE", BLUE, pick_colour(3))
check("4 bounces starts again at RED", RED, pick_colour(4))
check("13 bounces is YELLOW", YELLOW, pick_colour(13))

print("")
print("ROLE B: Rules    boost_speed()")
check("bounce 3: no boost", 4, boost_speed(4, 3))
check("bounce 5, moving right: one faster", 5, boost_speed(4, 5))
check("bounce 10, moving left: one faster to the left", -5, boost_speed(-4, 10))
check("bounce 7, moving left: no boost", -6, boost_speed(-6, 7))
check("bounce 15 at top speed: stays at MAX_SPEED", MAX_SPEED, boost_speed(MAX_SPEED, 15))
check("bounce 20 at top speed to the left: stays at -MAX_SPEED", 0 - MAX_SPEED, boost_speed(0 - MAX_SPEED, 20))

print("")
print("ROLE C: Detector    is_touching()")
check("boxes in the same spot", True, is_touching(100, 100, 100, 100))
check("boxes partly overlapping", True, is_touching(100, 100, 130, 140))
check("box 2 just inside box 1 on the right", True, is_touching(100, 100, 159, 100))
check("box 2 far to the right", False, is_touching(100, 100, 200, 100))
check("box 2 far to the left", False, is_touching(300, 100, 100, 100))
check("box 2 far below", False, is_touching(100, 100, 100, 200))
check("same column but far apart up and down", False, is_touching(100, 100, 140, 300))
check("same row but far apart side to side", False, is_touching(100, 100, 400, 120))

print("")
print("ROLE C: Detector    background_colour()")
check("touching gives FLASH", FLASH, background_colour(True))
check("not touching gives DARK", DARK, background_colour(False))

print("")
print("Studio total: " + str(passed) + " out of " + str(total) + " checks passed")
if passed == total:
    print("Everything passes. Run bounce_lab.py and play your game.")
