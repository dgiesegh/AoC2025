with open("day11.txt") as f:
    lines = f.readlines()

nodes = {}
for l in lines:
    node, outs = l.split(": ")
    outs = outs.strip().split(" ")
    nodes[node] = outs
nodes["out"] = []

def run_search(start):
    n_paths = {n: 0 for n in nodes.keys()}
    n_paths_0 = {n: 0 for n in nodes.keys()}
    n_paths_dac = {n: 0 for n in nodes.keys()}
    n_paths_fft = {n: 0 for n in nodes.keys()}
    n_paths_both = {n: 0 for n in nodes.keys()}
    n_paths[start] = 1
    n_paths_0[start] = 1
    n_paths_dac[start] = 0
    n_paths_fft[start] = 0
    n_paths_both[start] = 0
    current = None
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == "out":
            continue
        new = nodes[current]
        for n in new:
            n_paths[n] += n_paths[current]
            if current == "dac":
                n_paths_dac[n] += n_paths_0[current] + n_paths_dac[current]
                n_paths_both[n] += n_paths_fft[current] + n_paths_both[current]
            elif current == "fft":
                n_paths_fft[n] += n_paths_0[current] + n_paths_fft[current]
                n_paths_both[n] += n_paths_dac[current] + n_paths_both[current]
            else:
                n_paths_0[n] += n_paths_0[current]
                n_paths_dac[n] += n_paths_dac[current]
                n_paths_fft[n] += n_paths_fft[current]
                n_paths_both[n] += n_paths_both[current]
            if n not in queue:
                queue.append(n)
        n_paths[current] = 0
        n_paths_0[current] = 0
        n_paths_dac[current] = 0
        n_paths_fft[current] = 0
        n_paths_both[current] = 0
    return n_paths["out"], n_paths_both["out"]

print("Solution 1:", run_search("you")[0], "\nSolution 2:", run_search("svr")[1])