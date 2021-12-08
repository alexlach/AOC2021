from collections import Counter

codes = open("08/input.txt").read().split("\n")

# part 1
# we can easily determine 1, 4, 7, and 8 because of their length
distinct_nums = {2: 1, 4: 4, 3: 7, 7: 8}
count_distinct_nums = 0
for code in codes:
    signals, outputs = code.split(" | ")
    outputs = outputs.split(" ")
    for output in outputs:
        if len(output) in distinct_nums:
            count_distinct_nums += 1
print(count_distinct_nums)

# part 2
numbers = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def find_cipher(signals):
    code_freq = Counter("".join(signals))
    code_freq = {v: k for k, v in code_freq.items()}
    freq_lookup = {
        4: "e",
        6: "b",
        9: "f",
    }
    cipher = {}  # this maps the true chars (keys) to the encoded chars (values)

    # learn the cipher for e, b, and f, since we know how often these occur in signal
    for known_freq in freq_lookup:
        cipher[freq_lookup[known_freq]] = code_freq[known_freq]

    # we can find the cipher for c by using the number one (which we know consists of c and f)
    one = [s for s in signals if len(s) == 2][0]
    cipher["c"] = one.replace(cipher["f"], "")

    # find cipher for a, since we know it's the only thing 7 has that 1 doesn't
    seven = [s for s in signals if len(s) == 3][0]
    cipher["a"] = seven.replace(cipher["c"], "").replace(cipher["f"], "")

    # find cipher for d using the number four
    four = [s for s in signals if len(s) == 4][0]
    cipher["d"] = [c for c in four if c not in cipher.values()][0]

    # find cipher for g using the number eight
    eight = [s for s in signals if len(s) == 7][0]
    cipher["g"] = [c for c in eight if c not in cipher.values()][0]

    return cipher


sum = 0
for code in codes:
    signals, outputs = code.split(" | ")
    signals = signals.split(" ")
    cipher = find_cipher(signals)
    decoder = {v: k for k, v in cipher.items()}

    decoded_output = []
    for char in outputs:
        if char == " ":
            decoded_output.append(" ")
        else:
            decoded_output.append(decoder[char])
    output_nums = "".join(decoded_output).split(" ")
    output_nums = [str(numbers.index("".join(sorted(a)))) for a in output_nums]
    decoded_num = int("".join(output_nums))
    sum += decoded_num
print(sum)
