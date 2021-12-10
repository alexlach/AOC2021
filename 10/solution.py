lines = open("10/input.txt").read().split("\n")

openers = ("{", "(", "[", "<")
closers = ("}", ")", "]", ">")
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def is_corrupted(line):
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        else:  # it's a closer
            ind = closers.index(char)
            matching_opener = openers[ind]
            if stack.pop() != matching_opener:
                return True, points[char], None
    return False, 0, stack


total_points = 0
incomplete_lines = []
completions = []
for line in lines:
    corrupt, new_points, completion = is_corrupted(line)
    total_points += new_points
    if not corrupt:
        incomplete_lines.append(line)
        completions.append(completion)

end_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
score_list = []
for ind, line in enumerate(incomplete_lines):
    total_score = 0
    end = reversed(completions[ind])
    for char in end:
        total_score *= 5
        total_score += end_points[char]
    score_list.append(total_score)
score_list.sort()
print(score_list[len(score_list) // 2])