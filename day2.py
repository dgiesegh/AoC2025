# Calculate all numbers which are n-fold repitions of a smaller number in range [start, stop]
def get_repeats_in_range(start, stop, n):
    ids = []
    for l in range(len(start), len(stop)+1):
        if l%n != 0:
            continue
        step = int(l / n)
        new_start = str(max(int(start), 10**(l-1)))
        new_stop = str(min(int(stop), 10**l - 1))
        for combi in range(int(new_start[:step]), int(new_stop[:step])+1):
            id = int(str(combi)*n)
            if id >= int(start) and id <= int(stop):
                ids.append(id)
    return ids

with open("day2.txt") as f:
    ranges = f.read().strip().split(",")

ids_1 = set()
ids_2 = set()
for r in ranges:
    start, stop = r.split("-")
    for l in range(2, len(stop)+1):
        ids = get_repeats_in_range(start, stop, l)
        for id in ids:
            ids_2.add(id)
            if l == 2:
                ids_1.add(id)

print("Solution 1:", sum(ids_1), "\nSolution 2:", sum(ids_2))
