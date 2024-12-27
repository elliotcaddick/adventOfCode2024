"""
--- Day 25: Code Chronicle ---
"""

def part_one(filename: str, verbose=False):
    schematics = {}
    
    with open(filename) as file:
        curr_schematic = []
        i = 0
        
        for line in file:
            line = line.strip()
            
            if line == "":
                schematics[i] = curr_schematic
                curr_schematic = []
                i += 1
                continue
            
            curr_schematic.append(list(line))
    
    locks = []
    keys = []
    for schematic in schematics.values():
        current = []
        
        # Lock
        if schematic[0].count('#') == 5 and schematic[-1].count('.') == 5:
            for i in range(len(schematic[0])):
                counter = 0
                for j in range(1, len(schematic)):
                    if schematic[j][i] == '#':
                        counter += 1
                current.append(counter)
            locks.append(current)
        
        # Key
        elif schematic[0].count('.') == 5 and schematic[-1].count('#') == 5:
            for i in range(len(schematic[0])):
                counter = 0
                for j in range(len(schematic) - 2, -1, -1):
                    if schematic[j][i] == '#':
                        counter += 1
                current.append(counter)
            keys.append(current)
    
    nb_unique_lock = 0
    for lock in locks:
        for key in keys:
            is_valid = True
            for x in range(len(lock)):
                if lock[x] + key[x] > 5:
                    is_valid = False
                    break
            if is_valid:
                nb_unique_lock += 1
    
    return nb_unique_lock



 

print(f"=== [PART 1] TEST ===")
print(f"Test: {part_one("day25/test/sample.txt")}")
print(f"=== [PART 1] PUZZLE RESULT ===")
print(f"Puzzle result: {part_one("day25/input/puzzle.txt")}")