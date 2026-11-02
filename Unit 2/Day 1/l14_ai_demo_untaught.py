# ICD2O Lesson 14: AI demo backup (teacher only)
# Show this if the live AI answer happens to use only taught constructs.
# Ask students to explain each line. Untaught here: while True, break,
# f-strings, a one-line if / else, and range with a step value.

import random

secret = random.randint(1, 20)
tries = 0

while True:
    guess = int(input("Guess a number from 1 to 20: "))
    tries += 1
    if guess == secret:
        print(f"Correct! You got it in {tries} tries.")
        break
    print("Too high" if guess > secret else "Too low")

for countdown in range(3, 0, -1):
    print(f"New round in {countdown}...")
