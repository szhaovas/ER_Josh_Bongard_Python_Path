import constants as c
from environment import ENV


class ENVs:
    def __init__(self, pb, pp):
        self.envs = {}
        for e in range(c.numEnvs):
            self.envs[e] = ENV(e % 4, pb, pp)
