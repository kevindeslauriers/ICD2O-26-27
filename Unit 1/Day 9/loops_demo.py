# ICD2O Lesson 9: Loops Continued
# while loops, loop until something changes, nested loops
#
# Run this file. Before each run, predict what the player will see.
# Then change a value in SECTION 1 and predict again.

# ------------------------------------------------------------
# SECTION 1: Values (change these)
# ------------------------------------------------------------
lives = 3
gems_needed = 18
rows = 3
cols = 4

# ------------------------------------------------------------
# SECTION 2: A while loop
# while checks the condition. If it is True, the body runs,
# then Python goes back up and checks again.
# Something in the body must change the condition, or it never stops.
# ------------------------------------------------------------
print("--- Section 2: while ---")
lives_left = lives
while lives_left > 0:
    print("Lives left:", lives_left)
    lives_left = lives_left - 1
print("Game over")

# ------------------------------------------------------------
# SECTION 3: The same job with for and with while
# for: you know how many times. while: you keep going until
# a condition changes.
# ------------------------------------------------------------
# print("--- Section 3: for and while ---")
# for wave in range(1, 4):
#     print("for: Wave", wave)

# wave = 1
# while wave <= 3:
#     print("while: Wave", wave)
#     wave = wave + 1

# ------------------------------------------------------------
# SECTION 4: Loop until something changes
# We do not know how many passes this takes. Each pass adds 5 gems.
# Trace it: write gems and passes for every pass before you run it.
# ------------------------------------------------------------
# print("--- Section 4: loop until ---")
# gems = 0
# passes = 0
# while gems < gems_needed:
#     gems = gems + 5
#     passes = passes + 1
#     print("Pass", passes, "gems =", gems)
# print("Done after", passes, "passes with", gems, "gems")

# ------------------------------------------------------------
# SECTION 5: When the condition is False at the start
# The body never runs, not even once.
# ------------------------------------------------------------
# print("--- Section 5: never runs ---")
# score = 50
# while score < 30:
#     print("Inside the loop")
#     score = score + 10
# print("Score:", score)

# ------------------------------------------------------------
# SECTION 6: Nested loops
# The inner loop runs ALL the way through for EACH pass of the outer loop.
# ------------------------------------------------------------
# print("--- Section 6: nested ---")
# tiles = 0
# for row in range(rows):
#     for col in range(cols):
#         print("row", row, "col", col)
#         tiles = tiles + 1
# print("Tiles:", tiles)

# ------------------------------------------------------------
# SECTION 7: A map made with nested loops
# row_text starts empty for each row, the inner loop adds one tile
# at a time, then the whole row is printed once.
# ------------------------------------------------------------
# print("--- Section 7: map ---")
# for row in range(rows):
#     row_text = ""
#     for col in range(cols):
#         row_text = row_text + "# "
#     print(row_text)

# ------------------------------------------------------------
# SECTION 8: Keep asking until the answer changes
# != means "is not equal to". Remove the # from these lines
# (select them, then Ctrl+/ in VS Code).
# ------------------------------------------------------------
# answer = ""
# while answer != "yes":
#     answer = input("Are you ready? Type yes: ")
# print("Let's go!")

# ------------------------------------------------------------
# SECTION 9: Traps. Remove the # from ONE trap at a time.
# If the terminal will not stop, click in the terminal and press Ctrl+C.
# ------------------------------------------------------------
# TRAP 1: nothing in the body changes energy. This never stops.
# energy = 10
# while energy > 0:
#     print("Running")
# print("Tired")

# TRAP 2: the body changes the value the wrong way. This never stops.
# lives_left = 3
# while lives_left > 0:
#     print("Lives left:", lives_left)
#     lives_left = lives_left + 1

# TRAP 3: row_text = "" is outside the outer loop, so it is never
# reset. Each row printed is longer than the one before.
# row_text = ""
# for row in range(rows):
#     for col in range(cols):
#         row_text = row_text + "# "
#     print(row_text)
