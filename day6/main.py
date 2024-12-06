"""
--- Day 6: Guard Gallivant ---
"""

def part_one(filename):
    the_map = []
    
    with open(filename) as file:
        for line in file:
            curr_line = (list(l for l in line.strip()))
            the_map.append(curr_line)
    
    x = None
    y = None
    for i in range(len(the_map)):
        for j in range(len(the_map[0])):
            if the_map[i][j] == "^":
                x = i
                y = j
                break
    
    def valid_coord(x, y):
        return 0 <= x < len(the_map) and 0 <= y < len(the_map[0])
    
    
    directions = {
        "^": (-1, 0, ">"),  # Up: decrease x, next direction is '>'
        ">": (0, 1, "v"),   # Right: increase y, next direction is 'v'
        "v": (1, 0, "<"),   # Down: increase x, next direction is '<'
        "<": (0, -1, "^")   # Left: decrease y, next direction is '^'
    }
    visited_coord = [(x, y)]
    while valid_coord(x, y):
        dx, dy = 0, 0

        if the_map[x][y] in directions:
            dx, dy, next_dir = directions[the_map[x][y]]
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(the_map) and 0 <= new_y < len(the_map[0]):  # Check bounds
                if the_map[new_x][new_y] == "#":  # Blocked
                    the_map[x][y] = next_dir
                else:  # Swap positions
                    the_map[x][y], the_map[new_x][new_y] = the_map[new_x][new_y], the_map[x][y]
                    x, y = new_x, new_y
                    if (x, y) not in visited_coord:
                        visited_coord.append((x, y))
            else:  # Out of bounds
                x, y = new_x, new_y
        
    return len(visited_coord)
                
        
# print(f"Part 1: {part_one("input/puzzle.txt")}")

from itertools import product
from collections import defaultdict

import inspect
import os
import re

EMPTY = "."
WALL = "#"
GUARD = "^"

DIRS = [
    (-1, 0),  # N
    (0, +1),  # W
    (+1, 0),  # S
    (0, -1),  # E
]


def count_steps(grid):
    n, m = len(grid), len(grid[0])

    x = 0
    for line in grid:
        if GUARD in line:
            guard_pos = (
                x,
                line.find(GUARD) if type(line) == str else line.index(GUARD),
            )
            break
        x += 1

    def within_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def move(x, y, direction):
        # 4 tries
        for _ in range(4):
            nx, ny = x + DIRS[direction][0], y + DIRS[direction][1]
            if within_bounds(nx, ny) and grid[nx][ny] == WALL:
                direction = (direction + 1) & 3
                continue
            return nx, ny, direction
        return False

    guard_x, guard_y = guard_pos
    guard_dir = 0  # starting position is N
    steps = defaultdict(set)
    while within_bounds(guard_x, guard_y):
        steps[(guard_x, guard_y)].add(guard_dir)
        move_res = move(guard_x, guard_y, guard_dir)
        if not move_res:
            return False
        guard_x, guard_y, guard_dir = move_res
        if guard_dir in steps[(guard_x, guard_y)]:
            return False

    return len(steps) - 1  # account for the last check


def part_two(filename):
    grid = []
    
    with open(filename) as file:
        for line in file:
            curr_line = (list(l for l in line.strip()))
            grid.append(curr_line)
    n, m = len(grid), len(grid[0])

    total = 0
    for x, y in product(range(n), range(m)):
        # https://i.imgur.com/beryVOv.png
        if grid[x][y] == EMPTY:
            grid_copy = [line[:] for line in grid]
            grid_copy[x][y] = WALL
            if not count_steps(grid_copy):
                total += 1

    return total

    
print(f"Part 2: {part_two("day6/input/puzzle.txt")}")