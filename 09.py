# A PART
folder = "examples"
folder = "input"
with open(folder+"/09.txt") as f:
    text = f.read()
counter = 0
counter2 = 0
commands = text.split('\n')
n = len(commands)
commands = [c.split(',') for c in commands]
commands = [(int(a), int(b)) for a, b in commands]
for i, (a, b) in enumerate(commands):
    for j, (c, d) in enumerate(commands[i:]):
        counter = max(counter, abs(a-c+1)*abs(b-d+1))
long, latt = [a for a, _ in commands], [b for _, b in commands]
long, latt = sorted(list(set(long))), sorted(list(set(latt)))
zipped_commands = [(long.index(a), latt.index(b)) for a, b in commands]
n, m = len(long), len(latt)
red_green_area = [['.' for _ in range(m)] for _ in range(n)]
def print_map():
    aa = [[red_green_area[j][i] for j in range(len(red_green_area))] for i in range(len(red_green_area[0]))]
    niz = ''
    for a in aa:
        niz += ''.join(a)
        niz += '\n'
    with open("demofile.txt", "w") as f:
        f.write(niz)
def write_to_map():
    non_changable = set()
    for i in range(len(zipped_commands)):
        a, b = zipped_commands[i-2]
        c, d = zipped_commands[i-1]
        if a == c:
            for j in range(min(b,d), max(b,d)+1):
                red_green_area[a][j] = 'X'
            if (zipped_commands[i-3][0] - a) * (zipped_commands[i][0] - a) > 0:
                non_changable.add((a,max(b,d)))
        else:
            for j in range(min(a,c), max(a,c)+1):
                red_green_area[j][b] = 'X'
    for i in range(n):
        outside = False
        for j in range(m-1):
            if red_green_area[i][j] == 'X' and red_green_area[i][j+1] != 'X' and (i,j) not in non_changable:
                outside = not outside
            if outside:
                red_green_area[i][j] = 'X'
                pass
            
    pass
write_to_map()
print_map()
def is_red_green_area(a,b,c,d):
    x = True
    for j in range(min(b,d), max(b,d)+1):
        if red_green_area[a][j] != 'X':
            x = False
        if red_green_area[c][j] != 'X':
            x = False
    for i in range(min(a,c), max(a,c)+1):
        if red_green_area[i][b] != 'X':
            x = False
        if red_green_area[i][d] != 'X':
            x = False
    return x
for i, (a, b) in enumerate(zipped_commands):
    for j, (c, d) in enumerate(zipped_commands[i:]):
        if is_red_green_area(a,b,c,d):
            counter2 = max(counter2, (abs(long[a]-long[c])+1)*(abs(latt[b]-latt[d])+1))
print(counter, counter2)