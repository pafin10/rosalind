from collections import defaultdict

def dfs(node, d, vis, cycle, used=0):
    # Mark the current node as visited
    vis[node] = True
    cycle.append(node)
    used += 1

    for neighbor in d[node]:
        if not vis[neighbor] and neighbor not in cycle:
            cycle, used = dfs(neighbor, d, vis, cycle, used)
        else: 
            continue

    return cycle, used



def find_cycles(adj):
    d = defaultdict(list)
    for a, b in adj: 
        d[a].append(b)
        d[b].append(a)
    a = next(iter(d))
    vis = {node: False for node in d}
    used = 0
    cycles = []
    while used < len(d.keys()):
        cycle, used = dfs(a, d, vis, [], used)
        cycles.append(cycle)
        for node in d.keys():
            if not vis[node]:
                a = node
                break
    return cycles, d


if __name__ == "__main__":
    adj = []
    with open("completing_a_tree.txt") as f: 
        n = int(f.readline().strip())
        for line in f:
            a, b = line.strip().split()
            a, b = int(a), int(b)
            adj.append((a, b))
    cycles, d = find_cycles(adj)
    print(len(cycles) - 1 + (n - len(d.keys())))