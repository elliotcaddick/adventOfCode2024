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


def part_two(filename):
    with open(filename) as f:
        disk_code = [int(i) for i in "".join(x.strip() for x in f)]

    d = {}
    frees = []

    counter = 0
    for i, r in enumerate(disk_code):
        start, end = counter, counter + r
        if i % 2 == 0:
            d[i//2] = (start, end)
        elif r > 0:
            frees.append((start, end))
        counter += r

    idx_ptr = max(d.keys())

    while idx_ptr >= 0:
        file_start, file_end = d[idx_ptr]
        file_len = file_end - file_start

        free_ptr = 0
        while free_ptr < len(frees):
            gap_start, gap_end = frees[free_ptr]
            if gap_start >= file_start:
                break

            gap_len = gap_end - gap_start
            if file_len <= gap_len:
                frees.pop(free_ptr)

                new_file_start, new_file_end = gap_start, gap_start + file_len
                new_gap_start, new_gap_end = new_file_end, gap_end

                d[idx_ptr] = (new_file_start, new_file_end)
                if new_gap_start != new_gap_end:
                    frees.insert(free_ptr, (new_gap_start, new_gap_end))
                break
            else:
                free_ptr += 1

        idx_ptr -= 1

    res = 0
    for k, (start, end) in d.items():
        res += sum(k*i for i in range(start, end))
    return res

print(f"Part 2: {part_two("input/puzzle.txt")}")