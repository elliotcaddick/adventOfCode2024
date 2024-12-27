"""
--- Day 19: Linen Layout ---
"""

def part_one(filename):
    towel_seq = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            
            if ',' in line:
                towels = [p.strip() for p in line.split(',')]
            elif  line != "":
                towel_seq.append(line)
    
    def can_form_towel(target, towels):
        def helper(remaining, towel_stack):
            if not remaining:
                return True, towel_stack
            for towel in towels:
                if remaining.startswith(towel):
                    result, used_towel = helper(remaining[len(towel):], towel_stack + [towel])
                    if result:
                        return True, used_towel
            return False, []
        return helper(target, [])

    result = 0
    for sequence in towel_seq:
        can_form, used_towel = can_form_towel(sequence, towels)
        if can_form:
            result += 1
    
    return result
        

    
    return possible_patterns
 

# print(f"Part 1: {part_one("day19/input/puzzle.txt")}")

import time
from collections import deque

def part_two(filename):
    start_time = time.time()

    result = []
    with open(filename) as f:
        for line in f:
            l = line.strip()
            result.append(l)

    input = set(result[0].split(', ')), result[2:]

    def design_possible_count(towels, design, cache):
        if design == "":
            return 1

        if (c := cache.get(design, None)) is not None:
            return c

        result = 0
        for towel in towels:
            if towel == design[:len(towel)]:
                result += design_possible_count(towels, design[len(towel):], cache)

        cache[design] = result
        return result

    return sum(design_possible_count(input[0], d, {}) for d in input[1])


print(f"=== [PART 2] TEST ===")
print(f"{part_two("day19/test/sample.txt")}")
print(f"=== [PART 2] PUZZLE RESULT ===")
print(f"Part 2: {part_two("day19/input/puzzle.txt")}")