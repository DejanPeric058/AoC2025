# A PART
folder = "examples"
folder = "input"
with open(folder+"/03.txt") as f:
    text = f.read()
commands = text.split('\n')
commands = [[int(a) for a in r] for r in commands]
output_joltage = 0
number_of_digits = 12
for row in commands:
    digits = [0 for _ in range(number_of_digits)]
    for i in range(len(row)-number_of_digits+1):
        for j, d in enumerate(digits):
            if row[i+j] > d:
                digits[j:] = row[i+j:i+number_of_digits]
    e = int(''.join([str(x) for x in digits]))
    output_joltage += e
print(output_joltage)