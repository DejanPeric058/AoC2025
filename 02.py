# A PART
with open("input/02.txt") as f:
    text = f.read()
counter = 0
commands = text.split(',')
commands = [x.split('-') for x in commands]
# commands = [(int(a), int(b)) for (a,b) in commands]
print(commands)
counter = 0
for a, b in commands:
    ai, bi = int(a), int(b)
    for d in range(ai,bi+1):
        ds = str(d)
        n =len(ds)
        if ds[:n//2] == ds[n//2:]:
            counter+=d
print(counter)
