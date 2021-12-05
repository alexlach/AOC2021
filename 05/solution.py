from collections import Counter

lines = open("05/input.txt").read().split("\n")
segments = [a.split(" -> ") for a in lines]

# parse input, and separate out segments that are vert or horz
segs = []
for segment in segments:
    x1, y1 = segment[0].split(",")
    x2, y2 = segment[1].split(",")
    segs.append((int(x1), int(y1), int(x2), int(y2)))
segs_vh = [s for s in segs if s[0] == s[2] or s[1] == s[3]]


def count_bad_points(segs):
    bad_points = []
    for seg in segs:
        seg_len = max(abs(seg[2] - seg[0]), abs(seg[3] - seg[1]))
        for h in range(0, seg_len + 1):
            if seg[2] > seg[0]:
                x = seg[0] + h
            elif seg[2] < seg[0]:
                x = seg[0] - h
            else:
                x = seg[0]
            if seg[3] > seg[1]:
                y = seg[1] + h
            elif seg[3] < seg[1]:
                y = seg[1] - h
            else:
                y = seg[1]
            bad_points.append((x, y))
    bad_dict = Counter(bad_points)
    return sum([1 for num in bad_dict.values() if num > 1])


print(count_bad_points(segs_vh))  # part 1
print(count_bad_points(segs))  # part 2