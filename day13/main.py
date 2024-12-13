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