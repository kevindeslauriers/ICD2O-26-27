# ICD2O Lesson 3: Variables Warm Up
# Tuesday, September 22
#
# Run this file (the play button, top right in VS Code).
# The output appears in the TERMINAL panel at the bottom.

# ------------------------------------------------------------
# SECTION 1: Five variables from a studio game
# ------------------------------------------------------------
player_name = "Nova"
score = 0
lives = 3
player_speed = 4.5
has_key = False

print("Player:", player_name)
print("Score:", score)
print("Lives:", lives)
print("Speed:", player_speed)
print("Has key:", has_key)

# ------------------------------------------------------------
# SECTION 2: What type is each one?
# type() tells you the type of any value.
# ------------------------------------------------------------
print(type(player_name))
print(type(score))
print(type(player_speed))
print(type(has_key))

# ------------------------------------------------------------
# SECTION 3: Worksheet Part B
# Write your prediction on paper FIRST. Then remove the # from
# ONE line at a time, save, and run.
# ------------------------------------------------------------
# print(3 + 4, type(3 + 4))                        # B1
# print(3 + 4.0, type(3 + 4.0))                    # B2
# print(10 / 2, type(10 / 2))                      # B3
# print("3" + "4", type("3" + "4"))                # B4
# print("Level " + "2", type("Level " + "2"))      # B5
# print(2 * 2.5, type(2 * 2.5))                    # B6
# print("Level " + 2)                              # B7 (read the LAST line of the red text)

# ------------------------------------------------------------
# SECTION 4: Updating a value
# Predict what the last line prints before you run it.
# ------------------------------------------------------------
score = score + 10
score = score + 10
lives = lives - 1
print("After two coins and one hit:", score, lives)
