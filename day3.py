def find_largest_joltage(bank, n_batteries):
    start = 0
    batteries = []
    for i in range(n_batteries-1, -1, -1):
        possible_bs = [int(x) for x in bank[start:len(bank)-i]]
        b = max(possible_bs)
        start = bank.index(str(b), start) + 1
        batteries.append(b)
    return int("".join([str(x) for x in batteries]))


with open("day3.txt") as f:
    banks = [b.strip() for b in f.readlines()]

solutions_1 = []
solutions_2 = []
for b in banks:
    joltage_1 = find_largest_joltage(b, 2)
    joltage_2 = find_largest_joltage(b, 12)
    solutions_1.append(joltage_1)
    solutions_2.append(joltage_2)

print("Solution 1:", sum(solutions_1), "\nSolution 2:", sum(solutions_2))