# Part 2
f = open("input.txt", "r")
increaseCount = 0
prevbefore3 = 99999
before2 = 99999
before1 = 99999
for x in f:
  if (int(x) > prevbefore3):
    increaseCount += 1
  prevbefore3 = before2
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
