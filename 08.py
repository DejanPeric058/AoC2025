# A PART
folder = "examples"
folder = "input"
with open(folder+"/08.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [[int(d) for d in c.split(',')] for c in commands]
# print(commands)
def distance(sez1, sez2):
    result = 0
    for x,y in zip(sez1,sez2):
        result += (x-y)**2
    return result**(0.5)
# print(distance([2,2,2], [3,3,3]))
def find_the_nearest(comms, n):
    sez = [(999999999,([],[])) for _ in range(n)]
    for i, c1 in enumerate(commands):
        for c2 in commands[i+1:]:
            dist = distance(c1,c2)
            if dist < sez[-1][0]:
                sez[-1] = (dist, (c1,c2))
                sez.sort()
    return [{str(s[1][0]), str(s[1][1])} for s in sez]
def join_circuits(nearest_list):
    circuits = [nearest_list[0]]
    for new_circuit in nearest_list[1:]:
        flag=True
        count = set()
        for i, circuit in enumerate(circuits):
            for c in new_circuit:
                if c in circuit:
                    circuits[i] = circuit.union(new_circuit)
                    flag=False
                    count.add(i)
        if flag:
            circuits.append(new_circuit)
        if len(count) == 2:
            circuits[min(count)] = circuits[min(count)].union(circuits[max(count)])
            circuits = circuits[:max(count)] + circuits[max(count)+1:]
        if len(circuits) == 1:
            return new_circuit
    print(new_circuit)
    return circuits
sez_of_the_nearest = find_the_nearest(commands, 6000)
c = join_circuits(sez_of_the_nearest)
print(c)
ff = [len(f) for f in c]
ff.sort(reverse=True)
# print(c,ff)
# print(ff[0]*ff[1]*ff[2])
print(51125*62719)