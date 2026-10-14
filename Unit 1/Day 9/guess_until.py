# ICD2O Lesson 9: Guess the Number, Unlimited
#
# On September 30 you copied the same block three times to get three
# guesses. Today a while loop does the repeating for you.
#
# Build this in stages. Run your program after every stage.
# Do not start a stage until the one before it works.
#
# You know: variables, input, int(), if / elif / else, and, or, not,
# for loops, random.randint(), and now while and != (is not equal to).

import random

# ============================================================
# EDIT ZONE: the secret and the range
# ============================================================
low = 1
high = 20
secret_number = random.randint(low, high)
# ============================================================

print("=================================")
print("     GUESS THE NUMBER: UNLIMITED")
print("=================================")
print("I am thinking of a number from", low, "to", high)


# ------------------------------------------------------------
# STAGE 1: keep asking
# Make a variable guess and set it to 0 BEFORE the loop.
# Write a while loop that keeps going while guess is not equal to
# secret_number. Inside the loop, ask for a guess as a whole number.
# After the loop, print "You got it!"
# ------------------------------------------------------------




# ------------------------------------------------------------
# STAGE 2: help the player
# Inside the loop, after the guess, print "Too high" or "Too low".
# Print nothing extra when the guess is right.
# ------------------------------------------------------------




# ------------------------------------------------------------
# STAGE 3: count the guesses
# Use the count pattern: a counter set to 0 before the loop,
# add 1 inside the loop. After the loop, print how many guesses it took.
# ------------------------------------------------------------




# ------------------------------------------------------------
# STAGE 4: a rating
# After the loop, print a rating based on the number of guesses:
# 4 or fewer: "Expert", 5 to 7: "Good", more than 7: "Keep practising"
# ------------------------------------------------------------




# ------------------------------------------------------------
# CHALLENGE: only 5 lives
# Give the player 5 lives. Each wrong guess costs a life.
# Change the while condition so the loop also stops when lives reach 0.
# After the loop, print a win message or a lose message that shows
# the secret number.
# ------------------------------------------------------------
