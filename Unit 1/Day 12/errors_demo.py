# ICD2O Lesson 10: Three kinds of errors
# Live demo. Uncomment ONE example at a time, predict, run, read the message,
# then comment it out again.

print("Program started")

# ------------------------------------------------------------
# SYNTAX ERRORS: Python cannot read the program, so NOTHING runs.
# "Program started" does not print.
# ------------------------------------------------------------

# Example 1: missing colon on the def line (SyntaxError)
# def show_lives(lives)
#     print("Lives:", lives)

# Example 2: the body is not indented (IndentationError)
# def show_score(score):
# print("Score:", score)

# ------------------------------------------------------------
# RUNTIME ERRORS: the program starts, then crashes on one line.
# Everything above that line runs. "Program started" DOES print.
# ------------------------------------------------------------

# Example 3: a misspelt name (NameError)
# def coin_value(level):
#     return level * 10
#
# print(coin_valu(2))

# Example 4: the wrong number of values in the call (TypeError)
# def damage_after_shield(hit, has_shield):
#     if has_shield:
#         return hit // 2
#     else:
#         return hit
#
# print(damage_after_shield(4))

# Example 5: joining a str and an int with + (TypeError)
# level = 3
# print("Level " + level)

# Example 6: int() on text that is not a whole number (ValueError)
# Type three (the word) when it asks.
# lives = int(input("Starting lives: "))

# ------------------------------------------------------------
# LOGIC ERRORS: no message at all. The program runs and the player
# sees the wrong thing. You only catch it by predicting first.
# ------------------------------------------------------------

# Example 7: brackets missing (Lesson 4). Should print 60.0.
# def average(a, b, c):
#     return a + b + c / 3
#
# print("Average:", average(30, 60, 90))

# Example 8: the total is reset inside the loop. Should print 60.
# def coins_for_level(level):
#     return level * 10
#
# total = 0
# for level in range(1, 4):
#     total = 0
#     total = total + coins_for_level(level)
# print("Total:", total)

print("Program finished")
