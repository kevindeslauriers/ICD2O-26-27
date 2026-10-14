# ICD2O Lesson 6: Guess the Number
# Wednesday, September 30
#
# Build this in four stages. The tutorial tells you what each stage needs.
# Run your program after every stage. Do not write stage 3 before stage 2 works.
#
# You know: variables, types, operators, input, int(), and now if / elif / else.
# You do NOT know loops yet, so stage 4 repeats code on purpose. That is fine
# today. On October 6 you will learn how to stop repeating yourself.

# ============================================================
# EDIT ZONE: the secret
# ============================================================
secret_number = 7
# ============================================================

print("=================================")
print("     GUESS THE NUMBER")
print("=================================")
print("I am thinking of a number from 1 to 10.")


# ------------------------------------------------------------
# STAGE 1: one guess, one decision
# Ask for a guess as a whole number, then print "You got it!" if it
# matches the secret. Nothing else yet.
# ------------------------------------------------------------
# guess = int(input("What is your guess? "))

# if guess == secret_number:
#     print("You got it!")



# ------------------------------------------------------------
# STAGE 2: add the other branch
# Add an else so a wrong guess is told it is wrong.
# ------------------------------------------------------------
# guess = int(input("What is your guess? "))

# if guess == secret_number:
#     print("You got it!")
# else:
#     print("Wrong!")



# ------------------------------------------------------------
# STAGE 3: three ways it can go
# Change your else into elif and else so a wrong guess is told whether
# it was too high or too low.
# ------------------------------------------------------------
guess = int(input("What is your guess? "))

if guess == secret_number:
    print("You got it!")
elif guess > secret_number:
    print("Too High")
else:
    print("Too Low")


