# A PART
folder = "examples"
folder = "input"
with open(folder+"/11.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [(c.split()[0].replace(':',''), c.split()[1:]) for c in commands]
edgeList = []
commands = sorted(commands)
nodes = [v1 for v1, _ in commands]
nodes.append('out')
def str_to_int(s, nodes):
    return nodes.index(s)
for v1, vertices in commands:
    edgeList.extend([[str_to_int(v1,nodes), str_to_int(v,nodes)] for v in vertices])
# Python Code to count paths from source 
# to destinattion using Topological Sort
from collections import deque

def countPaths(n, edgeList, source, destination):

    # Create adjacency list (1-based indexing)
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for u, v in edgeList:
        graph[u].append(v)
        indegree[v] += 1
    # Perform topological sort using Kahn's algorithm
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    topoOrder = []
    while q:
        node = q.popleft()
        topoOrder.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Array to store number of ways to reach each node
    ways = [0] * (n + 1)
    ways[source] = 1

    # Traverse in topological order
    for node in topoOrder:
        for neighbor in graph[node]:
            ways[neighbor] += ways[node]

    return ways[destination]

if __name__ == "__main__":

    n = len(nodes)-1


    source = str_to_int('svr',nodes)
    destination = str_to_int('out',nodes)
    fft = str_to_int('fft',nodes)
    dac = str_to_int('dac',nodes)
    
    src_fft = countPaths(n, edgeList, source, fft)
    dac_dst = countPaths(n, edgeList, dac, destination)
    fft_dac = countPaths(n, edgeList, fft, dac)
    print(fft_dac)
    result = src_fft * fft_dac * dac_dst
    print(result)

