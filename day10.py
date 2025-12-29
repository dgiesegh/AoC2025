import numpy as np
import scipy.optimize as opt

def ind_to_binary(indicator):
    res = 0
    for i in range(len(indicator)):
        if indicator[i] == "#":
            res += 2**i
    return res

def schem_to_binary(schematic):
    res = 0
    for i in schematic:
        res += 2**int(i)
    return res

def get_trafomatrix(bin_schematics, joltage):
    res = [[0 for i in range(len(bin_schematics))] for j in range(len(joltage))]
    for i in range(len(bin_schematics)):
        for j, val in enumerate([b for b in format(bin_schematics[i], "0"+str(len(joltage))+"b")][::-1]):
            res[j][i] = int(val)
    return res                

with open("day10.txt") as f:
    lines = [[a[1:-1] for a in l.strip().split(" ")] for l in f.readlines()]

indicators = [ind_to_binary(l[0]) for l in lines]
schematics = [[schem_to_binary(s.split(",")) for s in l[1:-1]] for l in lines]
joltages = [[int(j) for j in l[-1].split(",")] for l in lines]

depths = []
for i in range(len(indicators)):
    queue = [0]
    queue2 = []
    seen = []
    depth = 1
    aim = indicators[i]
    buttons = schematics[i]
    found = False
    while not found:
        if len(queue) == 0:
            depth += 1
            queue, queue2 = queue2, queue
        state = queue.pop(0)
        for b in buttons:
            new_state = state ^ b
            if new_state == aim:
                found = True
                depths.append(depth)
                break
            if new_state not in seen:
                queue2.append(new_state)
                seen.append(new_state)

print("Solution 1:", sum(depths))

minvals = []
for i in range(len(lines)):
    print(f"Part 2: {i}/{len(lines)}", end="\r")
    T = np.array(get_trafomatrix(schematics[i], joltages[i]))
    b = joltages[i]
    res = opt.linprog(
        c = np.ones(len(schematics[i])),
        A_eq = T,
        b_eq = b,
        integrality = 1
    )
    if not res.success:
        raise RuntimeError("No optimization success")
    minvals.append(int(res.fun+0.5))
    if int(res.fun) != res.fun:
        print(i, "Warning: not int?", res.fun)

print("Solution 2:", sum(minvals))
