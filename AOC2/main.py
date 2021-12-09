# Running on repl.it? Switch to the shell > python AOC1/main.py

# Part 2
f = open("AOC2/input.txt", "r")

horizontal: int = 0
depth: int = 0
aim: int = 0
for x in f:
    command, num = x.split()[0], int(x.split()[1])
    if command == "forward":
        horizontal += num
        depth += aim*num
    elif command == "up":
        aim -= num
    else:
        aim += num
print(horizontal*depth)

# # Part 1
# f = open("AOC2/input.txt", "r")

# horizontal: int = 0
# depth: int = 0
# for x in f:
#     command, num = x.split()[0], int(x.split()[1])
#     if command == "forward":
#         horizontal += num
#     elif command == "up":
#         depth -= num
#     else:
#         depth += num
# print(horizontal*depth)
