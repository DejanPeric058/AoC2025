# A PART
folder = "examples"
folder = "input"
with open(folder+"/11.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [(c.split()[0].replace(':',''), c.split()[1:]) for c in commands]
# print(commands)
import networkx as nx
graph = nx.DiGraph()
for v1, vertices in commands:
    graph.add_edges_from([(v1, v) for v in vertices])
paths = nx.all_simple_paths(graph, source='you', target='out')
p = list(paths)
print(len(p))
