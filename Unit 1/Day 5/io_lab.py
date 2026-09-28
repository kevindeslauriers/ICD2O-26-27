# ICD2O Lesson 5: Input and Output Lab
# Monday, September 28
#
# Run this file. When the program stops with a flashing cursor in the
# TERMINAL panel, it is waiting for you. Type, then press Enter.

# ------------------------------------------------------------
# SECTION 1: print, two ways
# ------------------------------------------------------------
# user_name = "kdeslauriers"
# print("User:", user_name)
# print("User: " + user_name)

# ------------------------------------------------------------
# SECTION 2: input always hands back text
# ------------------------------------------------------------
# player_name = input("What is your name? ")
# print("Hello,", player_name)

# age_text = input("How old are you? ")
# print("You typed:", age_text)
# print("Its type is:", type(age_text))

# ------------------------------------------------------------
# SECTION 3: Worksheet Part B
# Predict first. Then remove the # from ONE line at a time.
# ------------------------------------------------------------
# print(age_text + 1)            # B4: predict the error, then read the last line
# print(age_text * 10)           # B5: this one does NOT crash. Why not?

# ------------------------------------------------------------
# SECTION 4: int(input()) turns the text into a number
# ------------------------------------------------------------
age = int(input("How old are you, in whole years? "))
print("Next year you will be", age + 1)
print("Its type is:", type(age))

# speed = float(input("How fast should the player move? "))
# print("Speed doubled is", speed * 2)

# ------------------------------------------------------------
# SECTION 5: Worksheet Part C
# Run this section and type letters instead of a number.
# Copy the LAST line of the error onto your worksheet.
# ------------------------------------------------------------
# lives = int(input("How many lives? "))
# print("You start with", lives, "lives.")
