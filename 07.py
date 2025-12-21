# A PART
folder = "examples"
folder = "input"
from pprint import pprint
with open(folder+"/07.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
#pprint(commands)
s_indexes = {commands[0].index('S')}
print('''......''')
for i, c in enumerate(commands[1:]):
    new_indexes = set()
    for s in s_indexes:
        if c[s] == '.':
            new_indexes.add(s)
            commands[i+1] = commands[i+1][:s] + '|' + commands[i+1][(s+1):]
            
        elif c[s] == '^':
            new_indexes.add(s-1)
            new_indexes.add(s+1)
            commands[i+1] = commands[i+1][:(s-1)] + '|' + commands[i+1][s:]
            commands[i+1] = commands[i+1][:(s+1)] + '|' + commands[i+1][(s+2):]
            counter+=1
    s_indexes = new_indexes
    
# pprint(commands)
# print(counter)
# print(commands)
edgeList = []
for i, row in enumerate(commands[:-1]):
    for j, x in enumerate(row):
        if x == '|' or x == 'S':
            if commands[i+1][j] == '^':
                edgeList.append([i*150 + j, (i+1)*150 + j+1])
                edgeList.append([i*150 + j, (i+1)*150 + j-1])
            else:
                edgeList.append([i*150 + j, (i+1)*150 + j])
for j, x in enumerate(commands[-1]):
    if x == '|':
        edgeList.append([(len(commands)-1)*150 + j, 9999999])

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

    n = 9999999


    source = commands[0].index('S')
    destination = 9999999
    # print(edgeList,source)
    result = countPaths(n, edgeList, source,destination)
    print(result)