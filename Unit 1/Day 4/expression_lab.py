# ICD2O Lesson 4: Expression Lab
# Thursday, September 24
#
# Run this file. Output appears in the TERMINAL panel at the bottom.

# ------------------------------------------------------------
# SECTION 1: The seven operators, all on 7 and 2
# ------------------------------------------------------------
# print("7 + 2  =", 7 + 2)
# print("7 - 2  =", 7 - 2)
# print("7 * 2  =", 7 * 2)
# print("7 / 2  =", 7 / 2)
# print("7 // 2 =", 7 // 2)
# print("7 % 2  =", 7 % 2)
# print("7 ** 2 =", 7 ** 2)

# ------------------------------------------------------------
# SECTION 2: Worksheet Part A and Part C
# Predict the value AND the type on paper first. Then remove the #
# from one line at a time, save, and run.
# ------------------------------------------------------------
# print(6 / 3, type(6 / 3))          # value and type
# print(6 // 3, type(6 // 3))
# print(6 % 4, type(6 % 4))
# print(2 ** 10, type(2 ** 10))
# print(7.0 // 2, type(7.0 // 2))
# print(9 % 3, type(9 % 3))

# ------------------------------------------------------------
# SECTION 3: Worksheet Part B, order of operations
# Predict first. Then uncomment one line at a time.
# ------------------------------------------------------------
print(2 + 3 * 4)                   # B1
print((2 + 3) * 4)                 # B2
print(10 - 4 - 3)                  # B3
print(2 ** 3 * 2)                  # B4
print(100 / 10 / 2)                # B5
print(10 + 20 % 7)                 # B6
print((10 + 20) % 7)               # B7

# ------------------------------------------------------------
# SECTION 4: Game maths
# These are the calculations running inside score_math.py.
# ------------------------------------------------------------
# total_seconds = 137
# minutes = total_seconds // 60
# seconds = total_seconds % 60
# print("Clock:", minutes, "minutes and", seconds, "seconds")

# screen_width = 960
# player_x = 1040
# print("Wrapped player_x:", player_x % screen_width)

# coins = 37
# extra_lives = coins // 10
# coins_towards_next = coins % 10
# print("Extra lives:", extra_lives, "  coins towards the next one:", coins_towards_next)

# ------------------------------------------------------------
# SECTION 5: Worksheet Part F, the broken average
# This line is wrong. Fix it, then run the file again.
# The three scores below should average to 30.
# ------------------------------------------------------------
# score_1 = 10
# score_2 = 20
# score_3 = 60
# average = score_1 + score_2 + score_3 / 3
# print("Average score:", average)
