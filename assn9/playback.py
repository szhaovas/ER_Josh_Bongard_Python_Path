import pickle
# from individual import INDIVIDUAL

f = open('robot.p', 'rb')
best = pickle.load(f)
f.close()
best.Evaluate(False)
print(best.fitness)
