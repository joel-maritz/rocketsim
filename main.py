import time
from sim import Simulation
from gui import ControlPanel

def display(sim):
    print('\033c')
    print('===============')
    print(' Mission Stats')
    print('===============')
    print()
    print(f'Engine Status: {'ON' if sim.engine_on else 'OFF'}')
    print(f'Throttle: {int(sim.throttle*100)}%')
    print()
    print(f'Velocity: {int(sim.speed)} m/s')
    print(f'Altitude: {int(sim.altitude)} m')
    print(f'Fuel: {int(sim.fuel)} kg')
    print()
    print(f"Time: T+{sim.time:.1f} s")
    print(f'Status: {'ACTIVE' if sim.active else 'LANDED'}')
    print()
    print('===============')

        
sim = Simulation()
gui = ControlPanel(sim)
dt = 0.1
simspeed = 3

while True:
    gui.update()
    sim.update(dt * simspeed)
    display(sim)
    time.sleep(dt)