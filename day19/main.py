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


# print(f"Part 2: {part_two("input/puzzle.txt")}")