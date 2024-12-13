"""
--- Day 13: Claw Contraption ---
"""

A_COST = 3
B_COST = 1

class Claw_Machine:
    def __init__(self):
        self.A = None
        self.B = None
        self.prize = None

def part_one(filename):
    claw_machines = []
    
    def parse_coordinates(line):
        parts = line.split(':')[1].replace('+', '=').split(',')
        x = y = 0
        for coord in parts:
            key, value = coord.split('=')
            if key.strip() == "X":
                x = int(value)
            elif key.strip() == "Y":
                y = int(value)
        return x, y
    
    with open(filename) as file:
        curr_machine = Claw_Machine()
        for line in file:
            line = line.strip()
            if line != "":
                if "Button A" in line:
                    curr_machine.A = parse_coordinates(line)
                elif "Button B" in line:
                    curr_machine.B = parse_coordinates(line)
                elif "Prize" in line:
                    curr_machine.prize = parse_coordinates(line)
                    claw_machines.append(curr_machine)
                    curr_machine = Claw_Machine()
    
    total_tokens = 0
    for machine in claw_machines:
        ax, ay = machine.A
        bx, by = machine.B
        px, py = machine.prize
        found = False
        for i in range(101):
            if found:
                break
            for j in range(101):
                if i * ax + j * bx == px and i * ay + j * by == py:
                    total_tokens += i * A_COST + j * B_COST
                    found = True
                    break
    
    return total_tokens
 

# print(f"Part 1: {part_one("input/puzzle.txt")}")


A_COST = 3
B_COST = 1
OFFSET = 10000000000000

class Claw_Machine:
    def __init__(self):
        self.A = None
        self.B = None
        self.prize = None

def part_two(filename):
    claw_machines = []
    
    def parse_coordinates(line, offset=0):
        parts = line.split(':')[1].replace('+', '=').split(',')
        x = y = 0
        for coord in parts:
            key, value = coord.split('=')
            if key.strip() == "X":
                x = int(value) + offset
            elif key.strip() == "Y":
                y = int(value) + offset
        return x, y
    
    def solve_equation(ax, ay, bx, by, px, py):
        det = ax * by - ay * bx
        if det == 0:
            return None
        det_i = px * by - py * bx
        det_j = ax * py - ay * px
        if det_i % det != 0 or det_j % det != 0:
            return None
        i = det_i // det
        j = det_j // det
        return i, j
    
    with open(filename) as file:
        curr_machine = Claw_Machine()
        for line in file:
            line = line.strip()
            if line != "":
                if "Button A" in line:
                    curr_machine.A = parse_coordinates(line)
                elif "Button B" in line:
                    curr_machine.B = parse_coordinates(line)
                elif "Prize" in line:
                    curr_machine.prize = parse_coordinates(line, OFFSET)
                    claw_machines.append(curr_machine)
                    curr_machine = Claw_Machine()
    
    total_tokens = 0
    
    for machine in claw_machines:
        ax, ay = machine.A
        bx, by = machine.B
        px, py = machine.prize
        result = solve_equation(ax, ay, bx, by, px, py)
        if result is not None:
            i, j = result
            if i >= 0 and j >= 0:
                total_tokens += i * A_COST + j * B_COST
    
    return total_tokens


print(f"Part 2: {part_two("input/puzzle.txt")}")