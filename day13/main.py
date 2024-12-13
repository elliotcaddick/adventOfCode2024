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
        coords = line.split(':')[1].split(',')
        x, y = 0, 0
        for coord in coords:
            if "+" in coord:
                parts = coord.split('+')
            elif "=" in coord:
                parts = coord.split('=')
            if "X" in parts[0]:
                x = int(parts[1])
            elif "Y" in parts[0]:
                y = int(parts[1])
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
        x, y = 0, 0
        is_found = False
        for i in range(1, 101):
            for j in range(1, 101):
                if i * machine.A[0] + j * machine.B[0] == machine.prize[0]\
                    and i * machine.A[1] + j * machine.B[1] == machine.prize[1]:
                        total_tokens += (i * A_COST) + (j * B_COST)
                        is_found = True
                        break
            if is_found:
                break
    
    return total_tokens
 
         
# print(f"Part 1: {part_one("input/puzzle.txt")}")