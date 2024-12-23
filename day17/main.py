"""
--- Day 17: Chronospatial Computer ---
"""

from math import trunc

def part_one(filename):
    registers = {}
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if "Register" in line:
                split_line = line.split(':')
                if "A" in split_line[0]:
                    registers["A"] = int(split_line[1])
                elif "B" in split_line[0]:
                    registers["B"] = int(split_line[1])
                elif "C" in split_line[0]:
                    registers["C"] = int(split_line[1])
            elif "Program" in line:
                programs = [int(i) for i in line.split(':')[1].split(',')]
    
    # Opcode 0
    def adv(operand):
        numerator = registers["A"]
        denominator = 2 ** operand
        return trunc(numerator / denominator)
    
    # Opcode 1
    def bxl(operand):
        return registers["B"] ^ operand
    
    # Opcode 2
    def bst(operand):
        return operand % 8
    
    # Opcode 3
    def jnz(operand):
        if registers["A"] == 0:
            return None
        else:
            return operand
    
    # Opcode 4
    def bxc():
        return registers["B"] ^ registers["C"]
    
    # Opcode 5
    def out(operand):
        return operand % 8
    
    # Opcode 6
    def bdv(operand):
        numerator = registers["A"]
        denominator = 2 ** operand
        return trunc(numerator / denominator)
    
    # Opcode 7
    def cdv(operand):
        numerator = registers["A"]
        denominator = 2 ** operand
        return trunc(numerator / denominator)

    output = []
    i = 0
    while i < len(programs):
        has_jumped = False
        opcode = programs[i]
        operand = programs[i+1]
        
        if operand == 4:
            operand = registers["A"]
        elif operand == 5:
            operand = registers["B"]
        elif operand == 6:
            operand = registers["C"]
        
        if opcode == 0:
            registers["A"] = adv(operand)
        elif opcode == 1:
            registers["B"] = bxl(operand)
        elif opcode == 2:
            registers["B"] = bst(operand)
        elif opcode == 3:
            if jnz(operand) is not None:
                i = operand
                has_jumped = True
        elif opcode == 4:
            registers["B"] = bxc()
        elif opcode == 5:
            output.append(out(operand))
        elif opcode == 6:
            registers["B"] = bdv(operand)
        elif opcode == 7:
            registers["C"] = cdv(operand)
        
        if not has_jumped:
            i += 2
    
    final_str = ""
    for o in output:
        final_str += str(o) + ","
    
    return final_str[:-1]


""" print(f"Test 1: {part_one("day17/test/sample2.txt")}")
print(f"Test 2: {part_one("day17/test/sample3.txt")}")
print(f"Test 3: {part_one("day17/test/sample4.txt")}")
print(f"Test 4: {part_one("day17/test/sample5.txt")}")
print(f"Test 5: {part_one("day17/test/sample6.txt")}") """
""" print(f"=== [PART 1] TEST ===")
print(f"{part_one("day17/test/sample1.txt")}")
print(f"=== [PART 1] PUZZLE RESULT ===")
print(f"{part_one("day17/input/puzzle.txt")}") """

import re

def part_two(filename):
    with open(filename) as f:
        inp = f.read().split("\n\n")
        regs = [int(re.findall(r"\d+", i)[0]) for i in inp[0].split("\n")]
        prog = [int(i) for i in re.findall(r"\d+", inp[1])]

    def opcode(reg, prog):
        i = 0
        output = []

        while True:
            op= prog[i]
            li = prog[i+1]

            co = li
            if 3 <= co <= 6:
                co = reg[co-4]
            
            if op == 0:
                reg[0] //= (2 ** co)
            elif op == 1:
                reg[1] ^= li
            elif op == 2:
                reg[1] = co % 8
            elif op == 3:
                if reg[0] != 0:
                    i = li - 2
            elif op == 4:
                reg[1] = reg[1] ^ reg[2]
            elif op == 5: # out
                output += [ co % 8 ]
            elif op == 6: # bdv
                reg[1] = reg[0] // 2 ** co  
            elif op == 7: # cdv
                reg[2] = reg[0] // 2 ** co 
            
            i += 2
            if i >= len(prog):
                break
        
        return output, reg



    

        

print(f"=== [PART 2] TEST ===")
print(f"{part_two("day17/test/sample7.txt")}")
print(f"=== [PART 2] PUZZLE RESULT ===")
print(f"Part 2: {part_two("day17/input/puzzle.txt")}")