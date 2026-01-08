with open("day12.txt") as f:
    lines = f.readlines()[30:]

trivial_fit = 0
trivial_not_fit = 0
other = 0
for l in lines:
    size, nums = l.split(": ")
    size = [int(i) for i in size.split("x")]
    nums = [int(i) for i in nums.strip().split(" ")]
    area = size[0] * size[1]
    area_shapes_big = 9 * sum(nums)
    area_shapes_small = 7 * sum(nums)
    if area_shapes_big <= area:
        trivial_fit += 1
    elif area_shapes_small >= area:
        trivial_not_fit += 1
    else:
        other += 1

print(trivial_fit, trivial_not_fit, other)
print("Solution: ", trivial_fit)