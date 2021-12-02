depths = open("01/input.txt").read().split("\n")
depths = [int(a) for a in depths]

# part 1 - count how many depths are deeper than the depth before them
count = -1
prev_depth = 0
for depth in depths:
    if depth > prev_depth:
        count += 1
    prev_depth = depth
print(count)

# part 1, solved with list comprehensions
diffs = [dep - dep_os for dep, dep_os in zip(depths[:-1], depths[1:])]
print(sum(1 for i in diffs if i < 0))

# part 1, oneliner, noting that booleans can be parsed as ints
print(sum(a < b for a, b in zip(depths, depths[1:])))

# part 2, consider a sliding window of three measurements
mov_sum = [d1 + d2 + d3 for d1, d2, d3 in zip(depths[2:], depths[1:-1], depths[:-2])]
diffs = [dep - dep_os for dep, dep_os in zip(mov_sum[:-1], mov_sum[1:])]
print(sum(1 for i in diffs if i < 0))

# part 2, oneliner, noting that with sliding windows we can ignore the overlap:
# abc   <- window 1
#  bcd  <- window 2
# the only difference between these windows is a and d, since b and c are added to both
print(sum(a < d for a, d in zip(depths, depths[3:])))
