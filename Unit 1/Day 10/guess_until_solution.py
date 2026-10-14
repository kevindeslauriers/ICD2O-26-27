# ICD2O Lesson 9: Guess the Number, Unlimited (TEACHER SOLUTION)
# Stages 1 to 4, then the challenge version below (commented).

import random

low = 1
high = 20
secret_number = random.randint(low, high)

print("=================================")
print("     GUESS THE NUMBER: UNLIMITED")
print("=================================")
print("I am thinking of a number from", low, "to", high)

guess = 0
num_guesses = 0
while guess != secret_number:
    guess = int(input("Your guess: "))
    num_guesses = num_guesses + 1
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")

print("You got it!")
print("Guesses:", num_guesses)

if num_guesses <= 4:
    print("Rating: Expert")
elif num_guesses <= 7:
    print("Rating: Good")
else:
    print("Rating: Keep practising")

# ---------------- CHALLENGE: only 5 lives ----------------
# guess = 0
# lives = 5
# while guess != secret_number and lives > 0:
#     guess = int(input("Your guess: "))
#     if guess > secret_number:
#         print("Too high")
#         lives = lives - 1
#     elif guess < secret_number:
#         print("Too low")
#         lives = lives - 1
#     print("Lives:", lives)
#
# if guess == secret_number:
#     print("You got it!")
# else:
#     print("Out of lives. The number was", secret_number)
