"""
--- Day 9: Disk Fragmenter ---
"""

def part_one(filename):
    def parse_line(line):
        blocks = []
        id = 0
        for i, char in enumerate(line):
            count = int(char)
            if i % 2 == 0:
                blocks.extend([id] * count)
                id += 1
            else:
                blocks.extend(['.'] * count)
        return blocks
    
    with open(filename) as file:
        line = file.readline().strip()
    blocks = parse_line(line)
    
    last_block_index = len(blocks) - 1
    for i in range(len(blocks)):
        if blocks[i] == '.':
            while last_block_index > i and blocks[last_block_index] == '.':
                last_block_index -= 1
            if last_block_index > i:
                blocks[i], blocks[last_block_index] = blocks[last_block_index], blocks[i]
    
    checksum = sum(i * int(block) for i, block in enumerate(blocks) if block != '.')
    
    return checksum

# print(f"Part 1: {part_one("input/puzzle.txt")}")