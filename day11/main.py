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
