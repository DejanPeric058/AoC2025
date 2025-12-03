# A PART
folder = "examples"
# folder = "input"
with open(folder+"/01.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
