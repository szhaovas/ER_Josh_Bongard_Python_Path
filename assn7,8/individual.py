import pyrosim
import random
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random() * 2 - 1
        self.fitness = 0

    def Evaluate(self):
        sim = pyrosim.Simulator(play_paused=False, eval_time=100)
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()
        sensorData = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
        self.fitness = sensorData[-1]
