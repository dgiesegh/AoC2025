def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def argsort(l):
    return sorted(range(len(l)), key=l.__getitem__)

def merge_regions(reg, i, j):
    if i == j:
        return
    for el in reg[j]:
        reg[i].append(el)
    reg.pop(j)

with open("day8.txt") as f:
    points = [[int(x) for x in l.strip().split(",")] for l in f.readlines()]

# Distances
dists = []
for p1 in points:
    for p2 in points:
        dists.append(dist(p1, p2))
indices = [i for i in argsort(dists) if dists[i] != 0]

# Solution 1
n_connections = 1000
regions = [[str(p)] for p in points]
for i in range(0, 2*n_connections, 2):
    x = indices[i] // len(points)
    y = indices[i] % len(points)
    reg = None
    for j in range(len(regions)):
        if str(points[x]) in regions[j]:
            break
    for k in range(len(regions)):
        if str(points[y]) in regions[k]:
            break
    merge_regions(regions, j, k)
sizes_sorted = sorted([len(r) for r in regions])
solution1 = sizes_sorted[-1] * sizes_sorted[-2] * sizes_sorted[-3]

# Solution 2
while len(regions) > 1:
    i += 2
    x = indices[i] // len(points)
    y = indices[i] % len(points)
    reg = None
    for j in range(len(regions)):
        if str(points[x]) in regions[j]:
            break
    for k in range(len(regions)):
        if str(points[y]) in regions[k]:
            break
    merge_regions(regions, j, k)

solution2 = points[x][0] * points[y][0]

print("Solution 1:", solution1, "\nSolution 2:", solution2)