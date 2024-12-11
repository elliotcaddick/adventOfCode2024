"""
--- Day 11: Plutonian Pebbles ---
"""

def part_one(filename):
    with open(filename) as file:
        stones = [int(num) for line in file for num in line.strip().split()]
    
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                half_len = len(str(stone)) // 2
                new_stones.extend([int(str(stone)[:half_len]), int(str(stone)[half_len:])])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    
    return len(stones)
            
      
# print(f"Part 1: {part_one("input/puzzle.txt")}")


from collections import defaultdict
 
 
def get_stones(file):
    values = [int(x) for x in open(file).read().strip().split(' ')]
    dictionary = defaultdict(int)
 
    for i in range(len(values)):
        dictionary[values[i]] = 1
 
    return dictionary
 
 
def evolve(stones):
    output = defaultdict(int)
 
    for mark, quantity in stones.items():
        if mark == 0:  # rule 1
            output[1] += quantity
 
        elif len(str(mark)) % 2 == 0:  # rule 2
 
            midpoint = len(str(mark)) // 2
 
            left = int(str(mark)[:midpoint])
            right = int(str(mark)[midpoint:])
 
            output[left] += quantity
            output[right] += quantity
 
        else:  # rule 3
            output[mark * 2024] += quantity
 
    return output
 
 
def part_two(filename):
    stones = get_stones(filename)
    for i in range(75):
        stones = evolve(stones)
 
    return sum(stones.values())


# print(f"Part 2: {part_two("input/puzzle.txt")}")