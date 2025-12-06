def parse_calc(nums, op):
    sol = 0 if op == "+" else 1
    for num in nums:
        if op == "+":
            sol += num 
        else:
            sol *= num
    return sol

with open("day6.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

# data prep 1
numbers = []
for i in range(len(lines)-1):
    nums = ["".join([c for c in n if c != " "]) for n in lines[i].split(" ")]
    nums = [int(n) for n in nums if n != ""]
    numbers.append(nums)
operations = [op for op in lines[-1] if op != " "]

# solution 1
solutions1 = []
for i in range(len(operations)):
    nums = [num_line[i] for num_line in numbers]
    solutions1.append(parse_calc(nums, operations[i]))

# data prep 2
lens = [len(l) for l in lines]
lines_transposed = [[] for i in range(max(lens))]
for j in range(max(lens)):
    for i in range(len(lines)):
        lines_transposed[j].append(lines[i][j])

# solution 2
i = -1
solutions2 = []
nums = []
operation = "+"
while i < len(lines_transposed)-1:
    i += 1
    line = lines_transposed[i]
    if (line[-1] == "+" or line[-1] == "*"):
        operation = line[-1]
    num_str = "".join([c for c in line[:-1] if c != " "])
    if num_str == "":
        solutions2.append(parse_calc(nums, operation))
        nums = []
    else:
        nums.append(int(num_str))

print("Solution 1:", sum(solutions1), "Solution 2:", sum(solutions2))