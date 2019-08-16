import pyrosim
import random
import math
import numpy as np
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.random(4) * 2 - 1
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
        sensorData = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        self.fitness = sensorData[-1]
        del self.sim
        del self.robot

    def Mutate(self):
        target = self.genome[random.randint(0, 3)]
        # cannot be 'target' here because python cannot make a pointer point to a different value
        # it can only modify the pointed value based on its current state
        self.genome[random.randint(0, 3)] = random.gauss(
            target, math.fabs(target))

    def Print(self):
        print('[ID:', self.ID, ' ', 'Fitness:', self.fitness, ']', end=' ')
