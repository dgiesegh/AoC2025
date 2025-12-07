with open("day7.txt") as f:
    lines = [[c for c in l.strip()] for l in f.readlines()]

# Find start
start = []
for i in range(len(lines[0])):
    if lines[0][i] == "S":
        start = [0, i]
        break

# Solutions
positions = [start]
visited = set()
values = {str([i,j]): 0 for i in range(len(lines)) for j in range(len(lines[0]))}
values[str(start)] = 1
paths = 0
splits = 0
def visit(spot):
    if str(spot) not in visited:
        positions.append(spot)
    visited.add(str(spot))
while len(positions) > 0:
    positions.sort(key=lambda p: p[0])
    pos = positions.pop(0)
    if pos[0] >= len(lines)-1:
        paths += values[str([pos[0]-1, pos[1]])]
        continue
    if lines[pos[0]+1][pos[1]] == ".":
        new_pos = [pos[0]+1, pos[1]]
        visit(new_pos)
        if new_pos[0] < len(lines):
            values[str(new_pos)] += values[str(pos)]
    elif lines[pos[0]+1][pos[1]] == "^":
        splits += 1
        for d in [-1,1]:
            new_pos = [pos[0]+1, pos[1]+d]
            visit(new_pos)
            values[str(new_pos)] += values[str(pos)]

print("Solution 1:", splits, "Solution 2:", paths)