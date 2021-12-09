# Running on repl.it? Switch to the shell > python AOC1/main.py

# Part 2
f = open("AOC3/input.txt", "r")

count = [0]*12 # count stores the number of 1s in i-th bit
numLines = 0
for x in f:
    numLines += 1
    bits = list(x)
    for i in range(0, 12):
        count[i] += int(bits[i])

gammaRate = 0
epsilonRate = 0
for i in range(0, 12):
    if count[i] > (numLines//2): # 1 is most common
        gammaRate += pow(2, 11 - i) # binary to decimal
    else:
        epsilonRate += pow(2, 11 - i)
print(gammaRate*epsilonRate)

# # Part 1
# f = open("AOC3/input.txt", "r")

# count = [0]*12 # count stores the number of 1s in i-th bit
# numLines = 0
# for x in f:
#     numLines += 1
#     bits = list(x)
#     for i in range(0, 12):
#         count[i] += int(bits[i])

# gammaRate = 0
# epsilonRate = 0
# for i in range(0, 12):
#     if count[i] > (numLines//2): # 1 is most common
#         gammaRate += pow(2, 11 - i) # binary to decimal
#     else:
#         epsilonRate += pow(2, 11 - i)
# print(gammaRate*epsilonRate)




