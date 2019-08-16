import pickle
import constants as c
from population import POPULATION
# import matplotlib.pyplot as plt

parent = POPULATION(c.popSize)
parent.Initialize()
parent.Evaluate(True)
for g in range(c.numGens):
    print(g, end=' ')
    parent.Print()
    child = POPULATION(c.popSize)
    child.Fill_From(parent)
    child.Evaluate()
    parent.ReplaceWith(child)
bestIndividual = parent.Best_Individual()
parent.p[bestIndividual].Start_Evaluation(pb=False, pp=True)
parent.p[bestIndividual].Compute_Fitness()

f = open('robot.p', 'wb')
pickle.dump(parent, f)
f.close()
