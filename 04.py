# A PART
from pprint import pprint
folder = "examples"
folder = "input"
with open(folder+"/04.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
n, m = len(commands), len(commands[0])
commands = [['#' for _ in range(n+2)]] + [['#'] + [a for a in c] + ['#'] for c in commands] + [['#' for _ in range(n+2)]]
# pprint(commands)
def is_accessible(i,j):
    if commands[i][j] != '@':
        return 0
    count = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if commands[i+k][j+l] == '@':
                count +=1
    return 1 if count < 5 else 0

for i in range(1,n+1):
    for j in range(1,m+1):
        counter += is_accessible(i,j)
print(counter)