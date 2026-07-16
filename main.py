import time
from sim import Simulation
from gui import ControlPanel

def display(sim):
    print('\033c')
    print(f'Speed: {int(sim.speed)}')
    print(f'Altitude: {int(sim.altitude)}')
    print(f'Fuel: {int(sim.fuel)}')
    print(f"Time: T+{sim.time:.1f}s")
        
sim = Simulation()
gui = ControlPanel(sim)
dt = 0.1
simspeed = 3

while True:
    gui.update()
    sim.update(dt * simspeed)
    display(sim)
    time.sleep(dt)