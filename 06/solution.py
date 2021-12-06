from collections import Counter

fishies = open("06/input.txt").read().split(",")
fishies = [int(f) for f in fishies]


def sim_fish(fish_dict, days):
    print(f"Simulating with starting count: {fish_dict}")
    for day in range(days):
        fish_dict_update = {key: 0 for key in [0, 1, 2, 3, 4, 5, 6, 7, 8]}
        for age, count in fish_dict.items():
            if age == 0:
                fish_dict_update[8] += count  # same fish
                fish_dict_update[6] += count  # babby fish
            else:
                fish_dict_update[age - 1] += count
        fish_dict = fish_dict_update
    print(f"Final count is: {fish_dict}")
    return fish_dict


fish_dict = Counter(fishies)
print(sum(val for val in sim_fish(fish_dict, 80).values()))  # part 1
print(sum(val for val in sim_fish(fish_dict, 256).values()))  # part 2


# dumb slow stuipd sad way of solving part 1
# day1_fishies = fishies
# for day in range(0, 80):
#     fishies_updated = []
#     for fish in day1_fishies:
#         if fish == 0:
#             fishies_updated.append(6)  # same fish
#             fishies_updated.append(8)  # babby fish
#         else:
#             fishies_updated.append(fish - 1)
#     day1_fishies = fishies_updated
# print(len(fishies_updated))