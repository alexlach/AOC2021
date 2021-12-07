positions = open("07/input.txt").read().split(",")
positions = [int(f) for f in positions]


# part 1
fuel_dict = {}
for center in range(min(positions), max(positions)):
    distances = [abs(center - pos) for pos in positions]
    fuel_dict[center] = sum(distances)
print(fuel_dict[min(fuel_dict, key=fuel_dict.get)])


def triangular_number(n):
    return n * (n + 1) // 2


# part 2
fuel_dict = {}
for center in range(min(positions), max(positions)):
    distances = [triangular_number(abs(center - pos)) for pos in positions]
    fuel_dict[center] = sum(distances)
print(fuel_dict[min(fuel_dict, key=fuel_dict.get)])
