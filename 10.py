# A PART
folder = "examples"
folder = "input"
with open(folder+"/10.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
# print(commands)
import itertools

class Machine:
    def __init__(self, config):
        self.config = config
        self.light_config = self.set_light_config()
        self.buttons = self.set_buttons()
        self.joltage = self.set_joltage()
        self.current_lights = self.light_config.replace('#','.')
        self.num_of_buttons = len(self.buttons)

    def __repr__(self):
        return 'Current lights: {c}, wanted lights {w}, buttons : {b}'.format(c=self.current_lights, w=self.light_config, b=self.buttons)

    def set_light_config(self):
        return self.config.split()[0]
    
    def set_buttons(self):
        return [[int(a) for a in c.replace('(','').replace(')','').split(',')] for c in self.config.split()[1:-1]]
    
    def set_joltage(self):
        return self.config.split()[-1]
    
    def apply_button(self,x):
        for light in x:
            if self.current_lights[light+1] == '.':
                self.current_lights = self.current_lights[:light+1] + '#' + self.current_lights[light+2:]
            else:
                self.current_lights = self.current_lights[:light+1] + '.' + self.current_lights[light+2:]

    def prepare_combinations(self,i):
        sez = []
        for comb in itertools.combinations(self.buttons, i):
            sez.append(list(comb))
        return sez
    
    def calculate_min_presses(self):
        for i in range(1,self.num_of_buttons+1):
            prepared_possible_combinations = self.prepare_combinations(i)
            for combination in prepared_possible_combinations:
                for x in combination:
                    self.apply_button(x)
                if self.current_lights == self.light_config:
                    for x in combination:
                        self.apply_button(x)
                    return i
                else:
                    for x in combination:
                        self.apply_button(x)

list_of_machines = []
for c in commands:
    list_of_machines.append(Machine(c))
for m in list_of_machines:
    counter += m.calculate_min_presses()
print(counter)