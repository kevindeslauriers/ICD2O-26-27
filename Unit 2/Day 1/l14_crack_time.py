# ICD2O Lesson 14: Crack time lab
# How long would it take to try every possible password?
# Rough figure: a gaming graphics card attacking a stolen password file
# can make about 10 billion guesses every second.





guesses_per_second = 10000000000

print("Password A: 8 characters, any of 95 keyboard symbols")
combinations = 95 ** 8
seconds = combinations // guesses_per_second
print("Possibilities:", combinations)
print("Days to try them all:", seconds // 86400)
print()

print("Password B: 16 lowercase letters")
combinations = 26 ** 16
seconds = combinations // guesses_per_second
print("Possibilities:", combinations)
print("Years to try them all:", seconds // 31536000)
print()

print("Lowercase letters only, by length")
for length in range(6, 17):
    seconds = (26 ** length) // guesses_per_second
    print(length, "letters:", seconds, "seconds,", seconds // 31536000, "years")
