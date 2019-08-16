import random
import math
import numpy as np
import constants as c
from environments import ENVs
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.random((5, 8)) * 2 - 1
        self.fitness = 0

    def Start_Evaluation(self, pb, pp):
        self.envs = ENVs(pb, pp).envs
        self.robots = {}
        for e in self.envs:
            self.robots[e] = ROBOT(self.envs[e].sim, self.genome)
            self.envs[e].sim.start()

    def Compute_Fitness(self):
        fitnessSum = 0
        for e in self.envs:
            self.envs[e].sim.wait_to_finish()
            fitnessSum += self.envs[e].sim.get_sensor_data(sensor_id=self.robots[e].L5)[-1]
        self.fitness = fitnessSum / c.numEnvs
        del self.envs
        del self.robots

    def Mutate(self):
        target_r = random.randint(0, 4)
        target_c = random.randint(0, 7)
        target = self.genome[target_r, target_c]
        # cannot be 'target' here because python cannot make a pointer point to a different value
        # it can only modify the pointed value based on its current state
        self.genome[target_r, target_c] = random.gauss(
            target, math.fabs(target))

        if self.genome[target_r, target_c] > 1:
            self.genome[target_r, target_c] = 1
        elif self.genome[target_r, target_c] < -1:
            self.genome[target_r, target_c] = -1

    def Print(self):
        print('[ID:', self.ID, ' ', 'Fitness:', self.fitness, ']', end=' ')
