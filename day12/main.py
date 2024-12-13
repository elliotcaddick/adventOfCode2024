"""
--- Day 12: Garden Groups ---
"""

from collections import deque

def part_one(filename):
    garden = []
    
    with open(filename) as file:
        for line in file:
            garden.append([g for g in line.strip()])
    
    rows, cols = len(garden), len(garden[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_cost = 0

    def bfs(start, plant_type):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        area = 0
        perimeter = 0
        
        while queue:
            x, y = queue.popleft()
            area += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    if garden[nx][ny] == plant_type and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif garden[nx][ny] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1
        
        return area, perimeter
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = garden[i][j]
                area, perimeter = bfs((i, j), plant_type)
                total_cost += area * perimeter
    
    return total_cost
                
            
# print(f"Part 1: {part_one("input/puzzle.txt")}")


# pylint: disable=C0114,C0116,C0301,C0209,W1514,C0414

from time import time as perf_counter
from typing import Any
import os


input_file = os.path.join(os.path.dirname(__file__), "input.txt")
# input_file = os.path.join(os.path.dirname(__file__), "test.txt")


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


def is_valid(p, max_x, max_y):
    x, y = p
    return 0 <= x < max_x and 0 <= y < max_y


def flood_fill(grid, p):

    max_x, max_y = len(grid[0]), len(grid)

    start_x, start_y = p
    crop = grid[start_y][start_x]

    visited = set()
    to_visit = [p]

    while to_visit:
        x, y = to_visit.pop()
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid((nx, ny), max_x, max_y) and grid[ny][nx] == crop and (nx, ny) not in visited:
                to_visit.append((nx, ny))

    return visited


def perimeter(points):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return sum((p[0]+dx, p[1]+dy) not in points for p in points for dx, dy in deltas)


def check_dir(points, p):
    px, py = p

    s1 = p in points and (px-1, py) not in points
    s2 = p in points and (px+1, py) not in points

    return s1, s2


def count_edges(points):

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    edges = 0

    for x in range(min(xs), max(xs) + 1):
        s1 = False
        s2 = False
        for y in range(min(ys), max(ys) + 1):
            ns1, ns2 = check_dir(points, (x, y))
            edges += int(ns1 and not s1 + ns2 and not s2)
            s1, s2 = ns1, ns2

    return edges


def get_boundries(points):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return set((p[0]+dx, p[1]+dy) for p in points for dx, dy in deltas if (p[0]+dx, p[1]+dy) not in points)


def count_corners(region):
    corners = set()
    kernels = [
        [(-1, 0), (0, -1), (-1, -1)],  # upper left
        [(1, 0), (0, -1), (1, -1)],  # upper right
        [(-1, 0), (0, 1), (-1, 1)],  # lower left
        [(1, 0), (0, 1), (1, 1)],  # lower right
    ]

    # get outer corners
    for px, py in region:
        for kernel in kernels:
            vals = [(px+kx, py+ky) for kx, ky in kernel]
            if all(v not in region for v in vals):
                corners.add((px, py, kernels.index(kernel)))

    inner_kernels = [
        [(-1, 0), (0, -1)],
        [(-1, 0), (0, 1)],
        [(1, 0), (0, -1)],
        [(1, 0), (0, 1)],
    ]
    inner_corners = set()
    # get inner corners
    for px, py in get_boundries(region):
        for kernel in inner_kernels:
            vals = [(px+kx, py+ky) for kx, ky in kernel]
            if all(v in region for v in vals):
                dx, dy = kernel[0][0]+kernel[1][0], kernel[0][1]+kernel[1][1]
                if (px+dx, py+dy) in region:
                    inner_corners.add(
                        (px+dx, py+dy, inner_kernels.index(kernel)))
                else:
                    (v1x, v1y), (v2x, v2y) = vals
                    dx, dy = v1x-v2x, v1y-v2y
                    d1 = [(-dx, 0), (0, dy)]
                    d2 = [(dx, 0), (0, -dy)]

                    inner_corners.add((v1x, v1y, inner_kernels.index(d1)))
                    inner_corners.add((v2x, v2y, inner_kernels.index(d2)))

    return len(corners) + len(inner_corners)


@profiler
def part_two(filename):
    with open(filename) as f:
        grid = [list(l.strip()) for l in f.readlines()]

    crops = []
    visited = set()
    for y, l in enumerate(grid):
        for x, _ in enumerate(l):
            if (x, y) not in visited:
                v = flood_fill(grid, (x, y))
                crops.append(v)
                visited |= v

    return sum(len(v) * count_corners(v) for v in crops)


# print(f"Part 2: {part_two("input/puzzle.txt")}")