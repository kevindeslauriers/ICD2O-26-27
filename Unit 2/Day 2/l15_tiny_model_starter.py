# ICD2O Lesson 15: Be the model
# A tiny language model that only knows 10 sentences.
# Step 1: count the training data on your handout (Part 3).
# Step 2: replace each ??? with a number from your counts.
# Step 3: run it a few times. Does it print the same sentences every time?

import random

for sentence in range(5):
    # Pick the word after "The player" (out of 10 sentences)
    roll = random.randint(1, 10)
    if roll <= ???:          # how many sentences use jumps?
        verb = "jumps"
    elif roll <= ???:        # jumps + runs
        verb = "runs"
    else:
        verb = "falls"

    # Pick the ending (out of 10 sentences)
    roll = random.randint(1, 10)
    if roll <= ???:          # how many sentences end with quickly?
        ending = "quickly"
    elif roll <= ???:        # quickly + again
        ending = "again"
    else:
        ending = "into the lava"

    print("The player", verb, ending)
