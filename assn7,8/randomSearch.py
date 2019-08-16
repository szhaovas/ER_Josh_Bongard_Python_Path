from individual import INDIVIDUAL
# import matplotlib.pyplot as plt

for i in range(0, 3):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)
# sensorData = sim.get_sensor_data(sensor_id=P2)
# print(sensorData)
# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-1, +2)
# plt.plot(sensorData)
# plt.show()
