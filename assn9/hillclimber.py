import copy
import pickle
from individual import INDIVIDUAL
# import matplotlib.pyplot as plt

parent = INDIVIDUAL()
parent.Evaluate(False)
for g in range(0, 100):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print('[g: ', g, ' ] ', '[pw: ', parent.genome, ' ] ',
          '[p: ', parent.fitness, ' ] ', '[c: ', child.fitness, ' ]')
    if child.fitness > parent.fitness:
        parent = child
        parent.fitness = child.fitness
        parent.Evaluate(False)
f = open('robot.p', 'wb')
pickle.dump(parent, f)
f.close()
# sensorData = sim.get_sensor_data(sensor_id=P2)
# print(sensorData)
# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-1, +2)
# plt.plot(sensorData)
# plt.show()
