"""
--- Day 15: Warehouse Woes ---
"""

dirs = {
    "v": (1,0),
    "^": (-1,0),
    ">": (0,1),
    "<": (0,-1)
}

def part_one(filename):    
    with open(filename) as file:
        warehouse = [l.strip() for l in file.readlines()]
        
    def score_grid(grid, char):
        score = 0
        for r in range(rows):
            for c in range(cols):
                if grid[(r,c)] == char:
                    score += 100 * r + c
        return score

    def get_grid():
        grid = dict()
        i = 0
        cols = len(warehouse[0])
        robot = None
        while i < len(warehouse):
            if warehouse[i] == "":
                i += 1
                break
            for j in range(len(warehouse[i])):
                if warehouse[i][j] == "@":
                    robot = (i,j)
                grid[(i,j)] = warehouse[i][j]
            i += 1
        rows = i - 1
        return grid, i, rows, cols, robot

    def try_move(grid, robot, dir):
        next_pos = (robot[0]+dir[0],robot[1]+dir[1])
        next_type = grid.get(next_pos, "#")
        if next_type == "#":
            return grid, robot
        elif next_type == ".":
            grid[robot] = "."
            grid[next_pos] = "@"
            return grid, next_pos
        else:
            # There is a box in the way, see if it is movable
            movable = False
            next_check_pos = (next_pos[0]+dir[0],next_pos[1]+dir[1])
            while True:
                next_check_type = grid.get(next_check_pos, "#")
                if next_check_type == "#":
                    break
                elif next_check_type == "O":
                    next_check_pos = (next_check_pos[0]+dir[0],next_check_pos[1]+dir[1])
                else:
                    grid[next_check_pos] = "O"
                    movable = True
                    break
            if movable:
                grid[robot] = "."
                grid[next_pos] = "@"
                return grid, next_pos
            return grid, robot
    
    grid, i, rows, cols, robot = get_grid()
    moves = "".join(warehouse[i:])
    
    for move in moves:
        grid, robot = try_move(grid, robot, dirs[move])
    
    return score_grid(grid, 'O')
    

print(f"Part 1: {part_one("input/puzzle.txt")}")


# print(f"Part 2: {part_two("input/puzzle.txt")}")