import pyrosim
import random
import math
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random() * 2 - 1
        self.fitness = 0

    def Evaluate(self, pb):
        sim = pyrosim.Simulator(
            play_blind=pb,
            play_paused=False,
            eval_time=100)
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()
        sensorData = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
        self.fitness = sensorData[-1]

    def Mutate(self):
        self.genome = random.gauss(self.genome, math.fabs(self.genome))
