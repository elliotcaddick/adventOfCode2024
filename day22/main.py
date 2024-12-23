"""
--- Day 22: Monkey Market ---
"""

from math import trunc

def part_one(filename, verbose=False):
    secret_numbers = []

    with open(filename) as file:
        for line in file:
            secret_numbers.append(int(line.strip()))

    def mix(secret_nb, value):
        return secret_nb ^ value
    
    def prune(secret_nb):
        return secret_nb % 16777216
    
    final_secret_numbers= []
    for secret_nb in secret_numbers:
        curr_secret_nb = secret_nb
        for _ in range(2000):
            mult = curr_secret_nb * 64
            mix1 = mix(curr_secret_nb, mult)
            prune1 = prune(mix1)

            div = prune1 // 32
            mix2 = mix(prune1, div)
            prune2 = prune(mix2)

            mult2 = prune2 * 2048
            mix3 = mix(prune2, mult2)
            prune3 = prune(mix3)

            curr_secret_nb = prune3

            if verbose:
                print(curr_secret_nb)
        final_secret_numbers.append(prune3)
    
    return sum(final_secret_numbers)
 

print(f"=== [PART 1] TEST ===")
print(f"{part_one("day22/test/sample.txt")}")
print(f"=== [PART 1] PUZZLE RESULT ===")
print(f"{part_one("day22/input/puzzle.txt")}")