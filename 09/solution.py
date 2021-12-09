terrain_rows = open("09/input.txt").read().split("\n")
terrain_rows = [[int(h) for h in row] for row in terrain_rows]
y_range = len(terrain_rows)
x_range = len(terrain_rows[0])

# part 1
def is_low_point(y, x):
    height = terrain_rows[y][x]
    if y > 0 and terrain_rows[y - 1][x] <= height:
        return False
    if y < y_range - 1 and terrain_rows[y + 1][x] <= height:
        return False
    if x > 0 and terrain_rows[y][x - 1] <= height:
        return False
    if x < x_range - 1 and terrain_rows[y][x + 1] <= height:
        return False
    return True


low_points = []
for y in range(y_range):
    for x in range(x_range):
        if is_low_point(y, x):
            low_points.append([y, x, 1 + terrain_rows[y][x]])
print(sum([t[2] for t in low_points]))

# part 2
def flood_fill(terrain, point):
    y = point[0]
    x = point[1]
    total_size = 0
    if terrain[y][x] != 9:
        terrain[y][x] = 9
        total_size += 1
        # recursively invoke flood fill on all surrounding cells:
        if x > 0:
            total_size += flood_fill(terrain, (y, x - 1))
        if x < len(terrain[y]) - 1:
            total_size += flood_fill(terrain, (y, x + 1))
        if y > 0:
            total_size += flood_fill(terrain, (y - 1, x))
        if y < len(terrain) - 1:
            total_size += flood_fill(terrain, (y + 1, x))
    return total_size


basin_sizes = []
for point in low_points:
    basin_sizes.append(flood_fill(terrain_rows, point))
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])