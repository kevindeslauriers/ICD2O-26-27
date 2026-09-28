pennies = 7454643

# how many of each coin so we minimise the number of coins
quarters = pennies // 25
# pennies = pennies % 25
pennies = pennies - quarters * 25

dimes = pennies // 10
# pennies = pennies % 10
pennies = pennies - dimes * 10


nickles = pennies // 5
# pennies = pennies % 5
pennies = pennies - nickles * 5


print("Pennies: ", pennies, " Nickles: ", nickles, " Dimes: ", dimes, " Quarters: ", quarters)



