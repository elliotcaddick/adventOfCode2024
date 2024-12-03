"""
--- Day 3: Mull It Over ---
"""

import re

def part_one(filename):
    result = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            all_mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

            for mul in all_mul:
                left, right = mul.replace("mul(", "").replace(")", "").split(",")
                result += int(left) * int(right)

    return result


print(f"Part 1: {part_one("day3/input/puzzle.txt")}")