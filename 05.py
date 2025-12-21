# A PART
folder = "examples"
# folder = "input"
with open(folder+"/05.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
br = commands.index('')
intervals = [x.split('-') for x in commands[:br]]
intervals = [(int(a), int(b)) for a, b in intervals]
numbers = [int(x) for x in commands[br+1:]]
#print(intervals)
#print(numbers)
def in_interval(x):
    for a, b in intervals:
        if x>a-1 and x<b+1:
            return 1
    return 0
for x in numbers:
    counter+=in_interval(x)
print(counter)
# B PART
counter = 0
joined_intervals = [intervals[0]]
for a, b in intervals:
    flaga, flagb = True, True
    l, d = -1, -1
    joined_intervals.sort()
    for i, (c, d) in enumerate(joined_intervals):
        if c <= a <= d:
            l = i
        elif joined_intervals[i-1][1] < a < c:
            l = i
            flaga = False
        if c <= b <= d:
            r = i
        elif joined_intervals[i-1][1] < b < c:
            r = i-1
            flagb = False
    if a < joined_intervals[0][0]:
        l = 0
        flaga = False
    if b < joined_intervals[0][0]:
        r = -1
        flagb = False
    if a > joined_intervals[-1][1]:
        l = len(joined_intervals)
        flaga = False
    if b > joined_intervals[-1][1]:
        r = len(joined_intervals)-1
        flagb = False
    joined_intervals.append((999999999999999999999999999999, 0))
    new_interval = (min(a, joined_intervals[l][0]),max(b, joined_intervals[r][1]))
    joined_intervals.pop()
    joined_intervals = joined_intervals[:l]+joined_intervals[r+1:]
    joined_intervals.append(new_interval)
print(sorted(joined_intervals))
for a, b in joined_intervals:
    counter+= b-a+1
print(counter)