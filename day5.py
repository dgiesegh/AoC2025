def merge_if_overlap(r1, r2):
    if r1[1] >= r2[0] and r2[1] >= r1[0]:
        return [[min(r1[0], r2[0]), max(r1[1], r2[1])]]
    else:
        return [r1, r2]

with open("day5.txt") as f:
    lines = [line.strip() for line in f.readlines()]
split = lines.index("")
ranges = lines[:split]
ids = lines[split+1:]

total = 0
ranges = [[int(x) for x in r.split("-")] for r in ranges]
for id in ids:
    for r in ranges:
        if int(id) >= r[0] and int(id) <= r[1]:
            total += 1
            break

while True:
    merged = False
    for i in range(len(ranges)-1):
        if merged: break
        for j in range(i+1, len(ranges)):
            if merged: break
            new = merge_if_overlap(ranges[i], ranges[j])
            if len(new) == 1:
                ranges[i] = new[0]
                ranges.pop(j)
                merged = True
    if not merged:
        break

total2 = sum([r[1]-r[0]+1 for r in ranges])

print("Solution 1:", total, "Solution 2:", total2)