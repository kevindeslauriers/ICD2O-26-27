# ICD2O Lesson 14: Annotation practice
# An AI wrote this program. Run it, then annotate it using the course format.
# Every line must be one you can explain.

import random

def roll_damage(low, high):
    return random.randint(low, high)

health = 50
turns = 0
while health > 0:
    hit = roll_damage(5, 12)
    health = health - hit
    turns += 1
    if health < 0:
        health = 0
    print("Turn", turns, "hit", hit, "health", health)
print("Defeated after", turns, "turns")
