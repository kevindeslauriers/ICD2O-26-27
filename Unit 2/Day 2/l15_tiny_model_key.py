# ICD2O Lesson 15: Be the model (teacher key)
# Training data counts: jumps 5, runs 3, falls 2. quickly 4, again 3, into the lava 3.

import random

for sentence in range(100):
    roll = random.randint(1, 10)
    if roll <= 5:            # 5 out of 10 sentences use jumps
        verb = "jumps"
    elif roll <= 8:          # 5 + 3 = 8
        verb = "runs"
    else:                    # rolls 9 and 10: 2 out of 10
        verb = "falls"

    roll = random.randint(1, 10)
    if roll <= 4:            # 4 out of 10 end with quickly
        ending = "quickly"
    elif roll <= 7:          # 4 + 3 = 7
        ending = "again"
    else:                    # rolls 8, 9, 10: 3 out of 10
        ending = "into the lava"

    print("The player", verb, ending)

# Things to point out:
# 1. Each run prints different sentences: the model picks likely words, with randomness.
# 2. "The player falls quickly" can appear, but it is NOT in the training data.
#    The model picks each word on its own, so it can make new combinations.
# 3. If the training data had 9 jumps, almost every sentence would say jumps.
#    The data decides what the model says (bias, Lesson 16).
