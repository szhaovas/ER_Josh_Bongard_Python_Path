import copy
import random
from individual import INDIVIDUAL


class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize

    def Initialize(self):
        for i in range(self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Evaluate(self, pb=True):
        for i in self.p:
            self.p[i].Start_Evaluation(pb)
        for i in self.p:
            self.p[i].Compute_Fitness()

    def Print(self):
        for i in self.p:
            if self.p[i] is not None:
                self.p[i].Print()
        print()

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:
                self.p[i] = other.p[i]

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Copy_Best_From(self, other):
        bestIndividual = None
        bestFitness = 0
        for i in other.p:
            if other.p[i].fitness > bestFitness:
                bestIndividual = i
                bestFitness = other.p[i].fitness
        self.p[0] = copy.deepcopy(other.p[bestIndividual])

    def Collect_Children_From(self, other):
        for i in range(1, self.popSize):
            self.p[i] = copy.deepcopy(other.Winner_Of_Tournament_Selection())
            self.p[i].Mutate()

    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0, other.popSize - 1)
        p2 = random.randint(0, other.popSize - 1)
        while p2 is p1:
            p2 = random.randint(0, other.popSize - 1)
        if other.p[p1].fitness > other.p[p2].fitness:
            return other.p[p1]
        else:
            return other.p[p2]
