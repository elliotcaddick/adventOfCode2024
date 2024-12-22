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


def part_two(filename):
    # Read towels and towel sequences from the file
    with open(filename) as file:
        lines = [line.strip() for line in file if line.strip()]
    towels = [p.strip() for p in lines[0].split(',')]
    towel_seq = lines[1:]

    # Find all combinations using memoization
    def find_all_towel_combinations(target, towels):
        memo = {}

        def helper(remaining):
            if remaining in memo:  # Check memoized results
                return memo[remaining]
            if not remaining:  # Base case: target is fully constructed
                return [[]]
            
            combinations = []
            for towel in towels:
                if remaining.startswith(towel):
                    sub_combinations = helper(remaining[len(towel):])
                    for sub_combination in sub_combinations:
                        combinations.append([towel] + sub_combination)
            
            memo[remaining] = combinations
            return combinations
        
        return helper(target)

    # Process towel sequences and count total arrangements
    total_arrangement = 0
    results = {}
    for sequence in towel_seq:
        combinations = find_all_towel_combinations(sequence, towels)
        results[sequence] = combinations
        total_arrangement += len(combinations)

    return total_arrangement



print(f"Part 2: {part_two("day19/input/puzzle.txt")}")