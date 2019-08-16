import pyrosim
import random
import math
import numpy as np
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.random((4, 8)) * 2 - 1
        self.fitness = 0

    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator(
            play_blind=pb,
            play_paused=False,
            eval_time=100)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        x = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=0)
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        self.fitness = math.sqrt(x[-1]**2 + y[-1]**2)
        del self.sim
        del self.robot

    def Mutate(self):
        target_r = random.randint(0, 3)
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
