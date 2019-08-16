import pyrosim
import constants as c


class ENV:
    def __init__(self, cond, pb, pp):
        self.sim = pyrosim.Simulator(
            play_blind=pb,
            play_paused=pp,
            eval_time=c.evalTime)
        if cond == 0:
            self.Place_Light_Source_To_The_Front()
        elif cond == 1:
            self.Place_Light_Source_To_The_Right()
        elif cond == 2:
            self.Place_Light_Source_To_The_Back()
        elif cond == 3:
            self.Place_Light_Source_To_The_Left()
        lightSource = self.sim.send_box(x=self.x, y=self.y, z=self.z, length=c.L, width=c.L, height=c.L, r=1, g=1, b=1)
        self.sim.send_light_source(body_id=lightSource)

    # if cond = 0
    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = 30 * c.L
        self.z = c.L / 2

    # if cond = 1
    def Place_Light_Source_To_The_Right(self):
        self.x = 30 * c.L
        self.y = 0
        self.z = c.L / 2

    # if cond = 2
    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = -30 * c.L
        self.z = c.L / 2

    # if cond = 3
    def Place_Light_Source_To_The_Left(self):
        self.x = -30 * c.L
        self.y = 0
        self.z = c.L / 2
