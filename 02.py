# A PART
with open("input/02.txt") as f:
    text = f.read()
counter = 0
commands = text.split(',')
commands = [x.split('-') for x in commands]
counter = 0
for a, b in commands:
    ai, bi = int(a), int(b)
    for d in range(ai,bi+1):
        ds = str(d)
        n =len(ds)
        for m in range(1,n//2+1):
            res = {ds[i:i + m] for i in range(0, n, m)}
            if len(res) == 1:
                counter+=d
                break
print(counter)
