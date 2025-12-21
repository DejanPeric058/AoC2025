# A PART
folder = "examples"
# folder = "input"
with open(folder+"/06.txt") as f:
    text = f.read()
from pprint import pprint
counter = 0
commands = text.split('\n')
numb = commands[:-1]
operators = commands[-1]
#commands = [c.split() for c in commands]
n, m = len(commands), len(commands[0])
numb = [[numb[j][i] for j in range(n-1)] for i in range(m)]
numb = [''.join(n).replace(' ', '') for n in numb]
new_numb = []
temp = []
for n in numb:
    if n == '':
        new_numb.append(temp)
        temp = []
    else:
        temp.append(int(n))
new_numb.append(temp)
operators = operators.split()
#print(new_numb,operators)
commands = [new_numb[i] + [operators[i]] for i in range(len(new_numb))]
commands
#commands = [[commands[i][j] for i in range(n)] for j in range(m)]
#pprint(commands)
def multiply(mylist):
    result = 1
    for x in mylist:
        result *= x
    return result
for c in commands:
    numbers = [int(x) for x in c[:-1]]
    if c[-1] == '*':
        counter += multiply(numbers)
    elif c[-1] == '+':
        counter += sum(numbers)
print(counter)