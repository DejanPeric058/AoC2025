# A PART
folder = "examples"
folder = "input"
with open(folder+"/12.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
from pprint import pprint
# pprint(commands)
class Present:
    def __init__(self, shape, name):
        self.shape = shape
        self.name = str(name)
        self.size = self.calculate_size()
    def __repr__(self):
        return str(self.shape) + ', ' + self.name
    def calculate_size(self):
        count = 0
        for row in self.shape:
            count += row.count('#')
        return count
class Region:
    def __init__(self, config):
        self.config = config
        self.length, self.heigth = self.calculate_heigth_and_length()
        self.area = self.length * self.heigth
        self.present_numbers = self.get_present_numbers()
    def __repr__(self):
        return self.config
    def calculate_heigth_and_length(self):
        l, h = self.config.split(':')[0].split('x')
        l, h = int(l), int(h)
        return l, h
    def get_present_numbers(self):
        return [int(x) for x in self.config.split(': ')[1].split(' ')]
    def can_fit_all_the_presents(self, presents):
        presents_size = 0
        for present, number_of_presents in zip(presents, self.present_numbers):
            presents_size += present.size * number_of_presents
        if 1.2 * presents_size >= self.area:
            return 0
        else:
            return 1
presents = []
regions = []
for i in range(6):
    shape = commands[i*5+1:i*5+4]
    presents.append(Present(shape=shape,name=i))
for c in commands[30:]:
    regions.append(Region(config=c))
for region in regions:
    counter += region.can_fit_all_the_presents(presents)
print(counter)
# pprint(presents)
# pprint(regions)