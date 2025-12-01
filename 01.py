# A PART
with open("input/01.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
start = 50
left_pointing = 0
instructions = [(x[0], int(x[1:])) for x in commands]
for d, s in instructions:
    if d == 'L':
        start, start_p = start - s, start
        zeros = (start_p-1)//100 - (start-1)//100
        start = start%100
    else:
        start, start_p = start + s, start
        zeros = start//100 - start_p//100
        start = start%100
    left_pointing += zeros
    # print(start, zeros,left_pointing, d, s)
print(left_pointing)
