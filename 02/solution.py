commands = open("02/input.txt").read().split("\n")

# part 1
position = 0
depth = 0
for cmd in commands:
    dir, val = cmd.split(" ")
    if dir == "forward":
        position = position + int(val)
    elif dir == "up":
        depth = depth - int(val)
    elif dir == "down":
        depth = depth + int(val)
print(position * depth)

# part 2
position = 0
depth = 0
aim = 0
for cmd in commands:
    dir, val = cmd.split(" ")
    if dir == "forward":
        position = position + int(val)
        depth += aim * int(val)
    elif dir == "up":
        aim -= int(val)
    elif dir == "down":
        aim += int(val)
print(position * depth)