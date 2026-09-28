# ICD2O Lesson 5: The Studio Fortune Teller
# Monday, September 28
#
# Your micro-game. It asks the player some questions and prints a fortune
# built from their answers. No if statements yet: every player gets the
# same shape of fortune, with their own words and numbers inside it.
#
# YOUR PROGRAM MUST HAVE:
#   1. a banner line printed before anything is asked
print("*"*44)
print("*"," "*12, "FORTUNE TELLER", " "*12,"*")
print("*"*44)

#   2. ask for the player's name
player_name = input("Please enter your name: ")
#   3. at least three input() questions
#   4. at least one int(input()) or float(input())
age = int(input("Hi " + player_name + ", how old are you? "))
colour = input("What is your favourite colour, " +  player_name + ": ")
mark = float(input(colour + " is a nice colour for a " + str(age) + " year old. What did you get on the math test: "))

#   5. at least one calculation that uses an answer the player typed
#   6. a fortune printed at the end that uses at least three of the answers

fortune = player_name + " your hair will turn the colour " + colour + " by the time you are " + str(age + 20) + "."
print (fortune)
#
# Test it twice with different answers before you call it done.




