def count_rolls(grid, spot):
    s = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if grid[spot[0]+i][spot[1]+j] == "@":
                    s += 1
    return s

def find_and_remove(grid, depth):
    if depth == 0:
        return 0
    total = 0
    to_remove = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == "@":
                s = count_rolls(grid, [i,j])
                if s < 4:
                    total += 1
                    to_remove.append([i,j])
    if total == 0:
        return 0
    for spot in to_remove:
        grid[spot[0]][spot[1]] = "."
    return total + find_and_remove(grid, depth-1)

with open("day4.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    grid = []
    grid.append("."*(len(lines[0])+2))
    for line in lines:
        grid.append("."+line+".")
    grid.append("."*(len(lines[0])+2))
grid = [list(row) for row in grid]

print("Solution 1:", find_and_remove([r.copy() for r in grid], 1), "\nSolution 2:", find_and_remove([r.copy() for r in grid], -1))