with open("day9.txt") as f:
    points = [[int(x) for x in p.split(",")] for p in f.readlines()]

for i, p in enumerate(points):
    p2 = points[(i+1)%len(points)]
    if abs(p[0]-p2[0]) > 10000:
        print(p, p2)

import matplotlib.pyplot as plt

plt.plot([p[0] for p in points], [p[1] for p in points])
plt.show()