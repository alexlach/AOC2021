positions = open("07/input.txt").read().split(",")
positions = sorted([int(f) for f in positions])

center = positions[len(positions) // 2]  # median minimizes sum(abs deviations)
distances = [abs(center - pos) for pos in positions]
print(sum(distances))  # part 1

tri_num = lambda n: abs(n) * (abs(n) + 1) // 2
mean = sum(positions) // len(positions)  # mean is provably within 0.5 of optimum
fuel_1 = sum([tri_num(mean - pos) for pos in positions])
fuel_2 = sum([tri_num(mean + 1 - pos) for pos in positions])
print(min(fuel_1, fuel_2))  # part 2

# part 2, slow way
# fuel_dict = {}
# for center in range(min(positions), max(positions)):
#     distances = [tri_num(abs(center - pos)) for pos in positions]
#     fuel_dict[center] = sum(distances)
# print(fuel_dict[min(fuel_dict, key=fuel_dict.get)])
