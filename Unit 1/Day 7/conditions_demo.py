# ICD2O Lesson 7: Conditions Demo
# Friday, October 2
#
# Run this file. Change the values in SECTION 1, run again, and
# predict what the player will see before each run.

# ------------------------------------------------------------
# SECTION 1: Values (change these)
# ------------------------------------------------------------
has_key = True
score = 20
has_shield = False
lives = 3

# ------------------------------------------------------------
# SECTION 2: A nested if
# The inner if is only checked when the outer condition is True.
# ------------------------------------------------------------
print("--- Section 2: nested ---")
if has_key:
    if score >= 30:
        print("The door opens.")
    else:
        print("You have the key, but you need a score of 30.")
else:
    print("Locked. You need the key.")

# ------------------------------------------------------------
# SECTION 3: The same door with and
# One condition, two questions. Shorter, but the else cannot
# say which part was missing.
# ------------------------------------------------------------
print("--- Section 3: and ---")
if has_key and score >= 30:
    print("The door opens.")
else:
    print("The door stays shut.")

# ------------------------------------------------------------
# SECTION 4: and, or, not on their own
# print shows True or False for each condition.
# ------------------------------------------------------------
print("--- Section 4: and, or, not ---")
print("has_key and score >= 30:", has_key and score >= 30)
print("has_key or score >= 30:", has_key or score >= 30)
print("not has_shield:", not has_shield)
print("lives > 0 and lives < 4:", lives > 0 and lives < 4)

# ------------------------------------------------------------
# SECTION 5: Two traps. Remove the # from the lines of ONE trap
# at a time (select the lines, then Ctrl+/ in VS Code).
# ------------------------------------------------------------
# TRAP 1: English lets you skip the second "lives". Python does not.
# if lives > 0 and < 4:
#     print("Still alive")

# TRAP 2: This runs every time, whatever the player types.
# answer = input("Open the chest? ")
# if answer == "yes" or "y":
#     print("You open the chest.")

# FIX for TRAP 2: a full comparison on each side of or.
# answer = input("Open the chest? ")
# if answer == "yes" or answer == "y":
#     print("You open the chest.")
