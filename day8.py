with open("day8.input.txt") as fin:
    grid = fin.read().strip().split()
# print(grid)

antennas = {}
for j, row in enumerate(grid):
    for i, frequency in enumerate(row):
        if frequency == ".":
            continue
        antennas[frequency] = antennas.get(frequency) or []
        antennas[frequency].append((j, i))

antinodes = set()
for frequency in antennas.keys():
    locations = antennas[frequency]
    print(f"frequency {frequency} at {len(locations)}! locs")
    # create all pairs
    for i_l, loc_a in enumerate(locations):
        for loc_b in locations[i_l + 1 :]:
            dist = tuple(map(lambda i, j: j - i, loc_a, loc_b))
            for side in [1, -1]:
                loc = loc_a if side == -1 else loc_b
                antinode = tuple(map(lambda x, d: x + (side * d), loc, dist))
                if (
                    antinode[0] < 0
                    or antinode[0] >= len(grid)
                    or antinode[1] < 0
                    or antinode[1] >= len(grid[0])
                    # or grid[antinode[0]][antinode[1]] != "."
                ):
                    continue
                antinodes.add(antinode)
for a in antinodes:
    line = grid[a[0]]
    grid[a[0]] = line[: a[1]] + "#" + line[a[1] + 1 :]
# print(grid)
print(len(antinodes))
