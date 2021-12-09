"""
You have a list of lines (your input). For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line segment is given in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

You need to determine the number of points where at least two lines overlap. In the above example, this is a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

import re


def main():
    """Solve the problem!"""
    lines = []
    with open("05/input.txt") as input_file:
        for line in input_file:
            lines.append(line)
    lines = sorted(lines)
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        x1, y1, x2, y2 = map(int, re.findall("[0-9]+", line))
        if x1 == x2:  # vertical line
            for i in range(min(y1, y2), max(y1, y2) + 1):
                grid[i][x1] += 1
        elif y1 == y2:  # horizontal line
            for i in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][i] += 1

    count = 0
    for row in grid:
        count += len([x for x in row if x > 1])

    print(count)


if __name__ == "__main__":
    main()
