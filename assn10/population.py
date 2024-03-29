from individual import INDIVIDUAL


class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        for i in range(popSize):
            self.p[i] = INDIVIDUAL(i)

    def Evaluate(self, pb=True):
        for i in self.p:
            self.p[i].Start_Evaluation(pb)
        for i in self.p:
            self.p[i].Compute_Fitness()

    def Print(self):
        for i in self.p:
            self.p[i].Print()
        print()

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:
                self.p[i] = other.p[i]
