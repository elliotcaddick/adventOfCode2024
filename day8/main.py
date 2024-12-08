"""
--- Day 8: Resonant Collinearity ---
"""

"""
def part_one(filename):
    frequencies_map = []

    with open(filename) as file:
        for line in file:
            frequencies_map.append([l for l in line.strip()])
    
    antennas = {}
    for i in range(len(frequencies_map)):
        for j in range(len(frequencies_map[0])):
            if frequencies_map[i][j] != ".":
                if frequencies_map[i][j] in antennas:
                    antennas[frequencies_map[i][j]].append((i, j))
                else:
                    antennas[frequencies_map[i][j]] = [(i, j)]

    antinodes = {}
    for key, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i != j:
                    x, y = coords[i]
                    a, b = coords[j]
                    dx, dy = (x-a, y-b)
                    if 0 <= x + dx < len(frequencies_map) and 0 <= y + dy < len(frequencies_map[0]) and frequencies_map[x+dx][y+dy] == ".":
                        if key in antinodes:
                            if (x+dx, y+dy) not in antinodes[key]:
                                antinodes[key].append((x+dx, y+dy))
                        else:
                            antinodes[key] = [(x+dx, y+dy)]
    
    nb_antinodes = 0
    for key in antinodes.keys():
        nb_antinodes += len(antinodes[key])

    return nb_antinodes
"""


import itertools

def part_one(filename):
    # check if position in bounds given width and height
    def in_bounds(pos, w, h):
        i = pos[0]
        j = pos[1]
        return i in range(h) and j in range(w)

    # read input_data from file
    with open(filename, "r") as file:
        input_data = [list(line.strip()) for line in file.readlines()]

    # get grid dimensions
    width = len(input_data[0])
    height = len(input_data)

    # antenna dictionary where k=frequency and v=list of positions
    antennas = {}
    for i in range(height):
        for j in range(width):
            freq, pos = input_data[i][j], [i, j]
            if freq != ".":
                if freq not in antennas.keys():
                    antennas[freq] = [pos]
                else:
                    antennas[freq].append(pos)

    # build list of unique antinode positions
    unique_antinodes = []
    for frequency in antennas.keys():
        positions = antennas[frequency]
        pairs = list(itertools.combinations(positions, 2))  # get unique pairs of positions

        for pair in pairs:
            a = pair[0]
            b = pair[1]
            slope = [b[0] - a[0], b[1] - a[1]]  # slope from a to b

            # one antinode is a minus the slope, other is b plus the slope
            antinodes = [[a[0] - slope[0], a[1] - slope[1]], [b[0] + slope[0], b[1] + slope[1]]]
            for antinode in antinodes:
                if antinode not in unique_antinodes and in_bounds(antinode, width, height):
                    unique_antinodes.append(antinode)

    return len(unique_antinodes)


# print(f"Part 1: {part_one("day8/input/puzzle.txt")}")


def part_two(filename):
    # check if position in bounds given width and height
    def in_bounds(pos, w, h):
        i = pos[0]
        j = pos[1]
        return i in range(h) and j in range(w)

    # read input_data from file
    with open(filename, "r") as file:
        input_data = [list(line.strip()) for line in file.readlines()]

    # get grid dimensions
    width = len(input_data[0])
    height = len(input_data)

    # antenna dictionary where k=frequency and v=list of positions
    antennas = {}
    for i in range(height):
        for j in range(width):
            freq, pos = input_data[i][j], [i, j]
            if freq != ".":
                if freq not in antennas.keys():
                    antennas[freq] = [pos]
                else:
                    antennas[freq].append(pos)

    # build list of unique antinode positions
    unique_antinodes = []
    for frequency in antennas.keys():
        positions = antennas[frequency]
        pairs = list(itertools.combinations(positions, 2))    # get unique pairs of positions

        for pair in pairs:
            a = pair[0]
            b = pair[1]
            slope = [b[0] - a[0], b[1] - a[1]]    # slope from a to b

            antinodes = [a, b]    # a and b are both antinodes of each other

            # get antinodes moving away from a
            for i in itertools.count(start=1):
                antinode = [a[0] - i * slope[0], a[1] - i * slope[1]]
                if not in_bounds(antinode, width, height):
                    break
                antinodes.append(antinode)

            # get antinodes moving away from b
            for i in itertools.count(start=1):
                antinode = [b[0] + i * slope[0], b[1] + i * slope[1]]
                if not in_bounds(antinode, width, height):
                    break
                antinodes.append(antinode)

            for antinode in antinodes:
                if antinode not in unique_antinodes:
                    unique_antinodes.append(antinode)

    return len(unique_antinodes)


print(f"Part 2: {part_two("day8/input/puzzle.txt")}")