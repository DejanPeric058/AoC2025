# A PART
folder = "examples"
folder = "input"
with open(folder+"/09.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
n = len(commands)
print(n * (n-1) // 2)
commands = [c.split(',') for c in commands]
commands = [(int(a), int(b)) for a, b in commands]
print(commands)
for i, (a, b) in enumerate(commands):
    for j, (c, d) in enumerate(commands[i:]):
        counter = max(counter, abs(a-c+1)*abs(b-d+1))
print(counter)