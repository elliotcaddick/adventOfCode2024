"""
--- Day 1: Historian Hysteria ---
"""

def part_one(filename):
    left_list = []
    right_list = []
    total_distance = 0
    with open(filename) as file:
        for line in file:
            left_nb, right_nb = line.strip().split()
            right_list.append(int(right_nb))
            left_list.append(int(left_nb))
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    return total_distance

# print(part_one("day1/input/puzzle.txt"))