
with open("day1.txt") as f:
    rotations = [line.strip() for line in f.readlines()]

i = 50
pw1 = 0
pw2 = 0
for r in rotations:
    dir = r[0]
    val = int(r[1:])
    nrot = val // 100
    val -= nrot*100
    pw2 += nrot
    if dir == "L":
        if val > i and i != 0:
            pw2 += 1
        i -= val
    elif dir == "R":
        if val > (100 - i) and i != 0:
            pw2 += 1
        i += val
    i %= 100
    if i == 0:
        pw1 += 1
        pw2 += 1

print("Solution 1:", pw1, "\nSolution 2:", pw2)