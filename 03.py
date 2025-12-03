# A PART
folder = "examples"
folder = "input"
with open(folder+"/03.txt") as f:
    text = f.read()
commands = text.split('\n')
commands = [[int(a) for a in r] for r in commands]
output_joltage = 0
for row in commands:
    first, second = 0, 0
    for i, a in enumerate(row):
        if a > first and i < len(row) -1:
            first = a
            second = row[i+1]
        elif a > second:
            second = a 
    # print(first,second)
    output_joltage += first*10 + second
print(output_joltage)
