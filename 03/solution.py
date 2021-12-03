codes = open("03/input.txt").read().split("\n")

# Part 1
eps = ""
for bit in range(0, len(codes[0])):
    one_count = 0
    for code in codes:
        if code[bit] == "1":
            one_count += 1
    if one_count > len(codes) / 2:
        eps += "1"
    else:
        eps += "0"
gam = ["0" if i == "1" else "1" for i in eps]
print(int("".join(gam), 2) * int("".join(eps), 2))

# Part 2
def find_code(bit1, bit2):
    codes_left = codes
    for bit in range(0, len(codes_left[0])):
        one_count = 0
        for code in codes_left:
            if code[bit] == "1":
                one_count += 1
        if one_count >= len(codes_left) / 2:
            fav_bit = bit1
        else:
            fav_bit = bit2
        codes_left = [x for x in codes_left if x[bit] == fav_bit]
        if len(codes_left) == 1:
            break
    return int(codes_left[0], 2)


print(find_code("1", "0") * find_code("0", "1"))