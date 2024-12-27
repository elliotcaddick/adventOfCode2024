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

def part_two(filename):
    with open(filename, 'r') as f:
        reg, prog = f.read().split('\n\n')

    prog = list(map(int, prog.split(': ')[1].split(',')))
    rega, regb, regc = (int(line.split(': ')[1]) for line in reg.splitlines())

    def get_combo(oper, rega, regb, regc):
        if 0 <= oper <= 3:
            return oper
        if oper == 4:
            return rega
        if oper == 5:
            return regb
        if oper == 6:
            return regc

    def run(prog, rega, regb, regc):
        ip = 0
        out = []
        while ip < len(prog):
            oper = prog[ip+1]
            combo = get_combo(oper, rega, regb, regc)
            match prog[ip]:
                case 0:
                    rega //= 2**combo
                case 1:
                    regb ^= oper
                case 2:
                    regb = combo%8
                case 3:
                    if rega:
                        ip = oper
                        continue
                case 4:
                    regb ^= regc
                case 5:
                    out.append(combo%8)
                case 6:
                    regb = rega//2**combo
                case 7:
                    regc = rega//2**combo
            ip += 2
        return out

    print(','.join(map(str, run(prog, rega, regb, regc))))

    rega = 0
    j = 1
    istart = 0
    while j <= len(prog) and j >= 0:
        rega <<= 3
        for i in range(istart, 8):
            if prog[-j:] == run(prog, rega+i, regb, regc):
                break
        else:
            j -= 1
            rega >>= 3
            istart = rega%8+1
            rega >>= 3
            continue
        j += 1
        rega += i
        istart = 0
    
    print(rega)
    


print(f"=== [PART 2] TEST ===")
print(f"{part_two("day17/test/sample7.txt")}")
print(f"=== [PART 2] PUZZLE RESULT ===")
print(f"Part 2: {part_two("day17/input/puzzle.txt")}")