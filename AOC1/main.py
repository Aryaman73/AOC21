# Running on repl.it? Switch to the shell > python AOC1/main.py

# Part 2
f = open("input.txt", "r")
increaseCount = 0
before3 = float('inf')
before2 = float('inf')
before1 = float('inf')
for x in f:
	if (int(x) > before3):
		increaseCount += 1
	before3 = before2
	before2 = before1
	before1 = int(x)
print(increaseCount)

# Part 1
# f = open("input.txt", "r")
# increaseCount = 0
# prev = 99999
# for x in f:
#   if (int(x) > prev):
#     increaseCount += 1
#   prev = int(x)
# print(increaseCount)
