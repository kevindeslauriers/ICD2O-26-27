import random

# for guess_number in range(1000):
#     print(random.randint(1,10)) 

# sum = 0
# for num in range(1,1001):
#     sum = sum + num
# print(sum)

numHeads = 0

numFlips = 100000
for coin in range(numFlips):
    if random.randint(0,1) == 1:
        numHeads += 1

print("Heads:", str((numHeads/numFlips) * 100)+"%")

