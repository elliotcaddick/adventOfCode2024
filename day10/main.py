"""
--- Day 10: Hoof It ---
"""

def part_one(filename):
    topographic_map = []
    
    with open(filename) as file:
        for line in file:
            topographic_map.append([int(l) for l in line.strip()])
    
    def find_trailheads(topographic_map):
        trailheads = []
        for i, row in enumerate(topographic_map):
            for j, height in enumerate(row):
                if height == 0:
                    trailheads.append((i, j))
        return trailheads
    
    def explore_trails(topographic_map, start):
        rows, cols = len(topographic_map), len(topographic_map[0])
        visited = set()
        reachable_nines = set()
        
        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            
            if topographic_map[x][y] == 9:
                reachable_nines.add((x, y))
                return
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and topographic_map[nx][ny] == topographic_map[x][y] + 1:
                    dfs(nx, ny)
        
        dfs(*start)
        return reachable_nines
    
    trailheads = find_trailheads(topographic_map)
    total_rating = 0
    
    for trailhead in trailheads:
        reachable_nines = explore_trails(topographic_map, trailhead)
        total_rating += len(reachable_nines)
    
    return total_rating
                
            
# print(f"Part 1: {part_one("input/puzzle.txt")}")

import time
from pathlib import Path 

def part_two(filename):
    start_time = time.time()
    cwd = Path(__file__).parent
    file = open(filename, "r").read().splitlines()

    field = []
    trailHeads = []
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    maxY = len(file)-1
    maxX = len(file[0])-1
    for y, line in enumerate(file):
        xLine = []
        for x, c in enumerate(line):
            xLine.append(int(c))
            if(c == "0"):
                trailHeads.append((x,y))
        field.append(xLine)
        

    def printField(positions: list, mark = "X",):
        if(len(field) > 20):
            return
        for y in range(len(field)):
            line = ""
            for x in range(len(field[y])):
                if((x,y) in positions):
                    line += mark
                else:
                    line += str(field[y][x])
            print(line)
        print()

    def checkOutOfBounds(pos: tuple):
        return (pos[0] < 0 or pos[0] >= len(field[0]) or pos[1] < 0 or pos[1] >= len(field))


    def addPosition(pos: tuple, dir: tuple):
        return (pos[0] + dir[0], pos[1] + dir[1])

    def getValue(pos: tuple):
        return field[pos[1]][pos[0]]

    def checkTrail(pos: tuple, prevValue: int):
        result = 0
        for dir in directions:
            nextPos = addPosition(pos, dir)
            if(checkOutOfBounds(nextPos)):
                continue
            value = getValue(nextPos)
            if(value != prevValue+1):
                continue
            if(value == 9):
                result += 1
                continue
            
            result += checkTrail(nextPos, value)
        return result

    result = 0
    while(True):
        if(len(trailHeads) == 0):
            break
        trailHead = trailHeads.pop(0)
        foundPeaks = checkTrail(trailHead, 0)
        result += (foundPeaks)

    return result


# print(f"Part 2: {part_two("input/puzzle.txt")}")