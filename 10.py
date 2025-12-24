# A PART
folder = "examples"
folder = "input"
with open(folder+"/10.txt") as f:
    text = f.read()
counter = 0
counter2 = 0
commands = text.split('\n')
# print(commands)
import itertools
import numpy as np
from scipy.optimize import linprog

class Machine:
    def __init__(self, config):
        self.config = config
        self.light_config = self.set_light_config()
        self.buttons = self.set_buttons()
        self.joltage = self.set_joltage()
        self.current_lights = self.light_config.replace('#','.')
        self.num_of_buttons = len(self.buttons)
        self.joltage_prepared = np.array([int(z) for z in self.joltage.replace('{','').replace('}','').split(',')])
        self.buttons_matrix = self.set_matrix()
        

    def __repr__(self):
        return 'Current lights: {c}, wanted lights {w}, buttons : {b}'.format(c=self.current_lights, w=self.light_config, b=self.buttons)

    def set_light_config(self):
        return self.config.split()[0]
    
    def set_matrix(self):
        ma = []
        for z in self.buttons:
            f = [0 for _ in range(len(self.joltage_prepared))]
            for x in z:
                f[x] = 1
            ma.append(f)
        return ma
    
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
    
    def min_integer_solution(self):
        a = [[self.buttons_matrix[j][i] for j in range(len(self.buttons_matrix))] for i in range(len(self.buttons_matrix[0]))]
        bounds = [(0,None) for _ in range(len(a[0]))]
        c = [1 for _ in range(len(a[0]))]
        res = linprog(c=c, A_eq=a,b_eq=self.joltage_prepared,bounds=bounds,integrality=1)
        minimum = res.fun
        return minimum
    
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

for i, m in enumerate(list_of_machines):
    # print('-----------------------')
    # print(i)
    counter += m.calculate_min_presses()
    counter2 += m.min_integer_solution()
    # print(counter2)
    # print(m.buttons_matrix)
    # print(m.joltage_prepared)
print(counter)
print(counter2)