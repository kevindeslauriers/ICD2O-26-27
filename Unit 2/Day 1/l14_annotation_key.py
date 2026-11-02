# ICD2O Lesson 14: Annotation practice, teacher key
# AI: Claude. I asked: "write a loop where a monster hits the player until health is 0"
# I changed: nothing

import random   # lets the program pick random numbers

def roll_damage(low, high):              # a function that picks one hit
    return random.randint(low, high)     # a whole number from low to high, both ends included

health = 50   # starting health
turns = 0     # counter, set to 0 before the loop
while health > 0:                # keep going until health runs out
    hit = roll_damage(5, 12)     # new random hit every turn, from 5 to 12
    health = health - hit        # take the hit away from health
    turns += 1                   # count this turn
    if health < 0:               # health can go below 0 on the last hit
        health = 0               # so the player never sees negative health
    print("Turn", turns, "hit", hit, "health", health)   # one line per turn
print("Defeated after", turns, "turns")   # runs once, after the loop ends

# Answer to the handout question: the last hit can take health below 0
# (for example 4 minus 9 is -5). Without the if, the last line shows a
# negative health such as "health -5". The loop still ends either way,
# because -5 > 0 is False.
