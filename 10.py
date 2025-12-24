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
        minimum = 999999999
        n1, m1 = len(self.buttons_matrix), len(self.buttons_matrix[0])
        bb = np.array(self.buttons_matrix)
        m = np.linalg.matrix_rank(bb)
        # print(m)
        for comb1 in itertools.combinations([i for i in range(n1)], m):
            for comb2 in itertools.combinations([i for i in range(m1)], m):
                # print(list(comb1),list(comb2), bb)
                comb = bb[list(comb1),:][:,list(comb2)]
                # print(np.linalg.det(comb),comb)
                if np.abs(np.linalg.det(comb)) > 5.551115123125776e-10:
                    # print(np.linalg.det(comb))
                    comb2 = list(comb2)
                    # print(comb, np.array(self.joltage_prepared)[comb2])
                    x = np.linalg.solve(np.transpose(comb),np.array(self.joltage_prepared)[comb2])
                    # x = [int(y) for y in x]
                    # print([int(y) for y in x],[int(np.abs(y)) for y in x])
                    # print(np.dot(np.transpose(bb[list(comb1),:]),x), np.array(self.joltage_prepared))
                    if min(x) >= 0 and np.abs(sum(np.dot(np.transpose(bb[list(comb1),:]),x) - np.array(self.joltage_prepared))) < 5.551115123125776e-5:
                        # print(np.abs(sum(np.dot(np.transpose(bb[list(comb1),:]),x) - np.array(self.joltage_prepared))))
                        # print(len(np.transpose(comb)),len(np.transpose(comb)[0]),x)
                        # print(np.dot(np.transpose(comb),x) , np.array(self.joltage_prepared)[comb2])
                        # print(np.dot(np.transpose(bb[list(comb1),:]),x) , np.array(self.joltage_prepared))
                        # print(np.transpose(comb),np.transpose(bb[list(comb1),:]),x)
                        # print(len(np.transpose(bb[list(comb1),:])),len(np.transpose(bb[list(comb1),:])[0]),x)
                        if sum([abs(t-np.round(t)) for t in x]) > 5.551115123125776e-5:
                            print(x)
                        z = x
                        minimum = min(sum(x), minimum)
        # print(z)
        # print(minimum)
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
    print('-----------------------')
    print(i)
    counter += m.calculate_min_presses()
    counter2 += m.min_integer_solution()
    # print(counter2)
    # print(m.buttons_matrix)
    # print(m.joltage_prepared)
print(counter)
print(counter2)
a = [[0,0,0,1],[0,1,0,1],[0,0,1,0],[0,0,1,1],[1,0,1,0],[1,1,0,0]]
b = np.array([3, 5, 4, 7])
# x = np.linalg.solve(a,b)
# print(x)
def min_integer_solution(a,b):
    minimum = 999999999
    n, m = len(a), len(a[0])
    for comb in itertools.combinations(a, m):
        if np.linalg.det(comb) != 0:
            x = np.linalg.solve(np.transpose(np.array(comb)),b)
            x = [int(y) for y in x]
            # print([int(y) for y in x],[int(np.abs(y)) for y in x])
            if [int(y) for y in x] == [int(np.abs(y)) for y in x]:
                minimum = min(sum(x), minimum)
    return minimum
# print(min_integer_solution(a,b))