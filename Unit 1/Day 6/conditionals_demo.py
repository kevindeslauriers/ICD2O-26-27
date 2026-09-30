# ICD2O Lesson 6: Conditionals Demo
# Wednesday, September 30
#
# Run this file. Then follow the tutorial: it tells you when to come back
# here and change something.

# ------------------------------------------------------------
# SECTION 1: One decision
# ------------------------------------------------------------
has_key = True

if has_key:
    print("The door opens.")

print("The program carries on either way.")

# ------------------------------------------------------------
# SECTION 2: Two ways it can go
# Change has_key above to False and run this again.
# ------------------------------------------------------------
if has_key:
    print("You walk through.")
else:
    print("Locked. Find the key.")

# ------------------------------------------------------------
# SECTION 3: More than two ways
# Change score and run it again. Try 0, 30, 100.
# ------------------------------------------------------------
score = 30

if score >= 100:
    print("Gold rank")
elif score >= 50:
    print("Silver rank")
elif score >= 10:
    print("Bronze rank")
else:
    print("No rank yet")

# ------------------------------------------------------------
# SECTION 4: Only ONE branch runs
# Both of these are true for score = 30, but only the first one prints.
# ------------------------------------------------------------
if score > 10:
    print("Over ten")
elif score > 20:
    print("Over twenty")

# ------------------------------------------------------------
# SECTION 5: Indentation decides what is inside
# The tutorial asks you to predict what changes if line 2 of this
# block is moved left. Try it after you have predicted.
# ------------------------------------------------------------
lives = 1

if lives < 1:
    print("Game over.")
    print("Your final score was " + str(score))

print("Thanks for playing.")
