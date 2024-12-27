"""
--- Day 24: Crossed Wires ---
"""

from collections import OrderedDict

def and_check(l: int, r: int):
    if l == 1 and r == 1:
        return 1
    return 0

def or_check(l: int, r: int):
    if l == 1 or r == 1:
        return 1
    return 0

def xor_check(l: int, r: int):
    if l != r:
        return 1
    return 0

def part_one(filename: str, verbose=False):
    wires = {}

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if ':' in line:
                wire_name, wire_value = line.split(':')
                wires[wire_name] = int(wire_value)
            elif "->" in line:
                condition, target = line.split(' -> ')
                left, operand, right = condition.split(' ')
                if operand == "AND":
                    wires[target] = and_check(wires[left], wires[right])
                elif operand == "OR":
                    wires[target] = or_check(wires[left], wires[right])
                elif operand == "XOR":
                    wires[target] = xor_check(wires[left], wires[right])
    
    z_wires = {}
    
    for key, value in wires.items():
        if "z" in key:
            z_wires[key] = value
    
    z_wires = OrderedDict(sorted(z_wires.items(), reverse=True))

    binary = ""

    for value in z_wires.values():
        binary += str(value)

    return int(binary, 2)

 

print(f"=== [PART 1] TEST ===")
print(f"Test 1: {part_one("day24/test/sample1.txt")}")
print(f"Test 2: {part_one("day24/test/sample2.txt")}")
print(f"=== [PART 1] PUZZLE RESULT ===")
print(f"Puzzle result: {part_one("day24/input/puzzle.txt")}")