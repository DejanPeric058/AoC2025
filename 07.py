# A PART
folder = "examples"
# folder = "input"
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
    
#pprint(commands)
print(counter)