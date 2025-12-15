def area(p1, p2):
    return (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)

def is_inside(p, corner1, corner2):
    return p[0] > min(corner1[0], corner2[0]) and p[0] < max(corner1[0], corner2[0]) and p[1] > min(corner1[1], corner2[1]) and p[1] < max(corner1[1], corner2[1])

with open("day9.txt") as f:
    points = [[int(x.strip()) for x in l.split(",")] for l in f.readlines()]

max_a = 0
max_a_2 = 0
n_rects = int(( len(points)**2 - len(points) ) / 2)
for i, p1 in enumerate(points[:-1]):
    for j, p2 in enumerate(points[(i+1):]):
        a = area(p1, p2)
        if a > max_a:
            max_a = a
        if p2 == [94918, 50338]:
            if p1[1] > 50338:
                if not any(is_inside(p, p1, p2) for p in points):
                    if a > max_a_2:
                        max_a_2 = a
        elif p1 == [94918, 48430]:
            if p2[1] < 48430:
                if not any(is_inside(p, p1, p2) for p in points):
                    if a > max_a_2:
                        max_a_2 = a

print("Solution 1:", max_a, "\nSolution 2:", max_a_2)