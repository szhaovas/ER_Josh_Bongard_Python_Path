import pyrosim

sim = pyrosim.Simulator(play_paused=True, eval_time=1000)
whiteobject = sim.send_cylinder(z=0.6, length=1.0, radius=0.1)
redObject = sim.send_cylinder(y=0.5, z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)
print(redObject)
sim.start()
sim.wait_to_finish()
