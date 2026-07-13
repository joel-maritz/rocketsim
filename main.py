import time
class Simulation:
    def __init__(self):
        self.fuel = 200
        self.fuelDecayRate = 5

        self.speed = 0
        self.altitude = 0

        # temporary thrust model
        self.gravity = 9.81
        self.thrust = self.gravity + 5
        
        self.weight = 1000
        self.maxSpeed = 1200 - self.weight

        self.time = 0
        self.active = True

    def update(self, dt):

        if self.fuel > 0:
            self.speed += self.thrust * dt
            self.fuel -= self.fuelDecayRate * dt

        self.speed -= self.gravity * dt

        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed

        self.altitude += self.speed * dt

        if self.altitude < 0:
            self.altitude = 0
            self.speed = 0
        if self.fuel < 0:
            self.fuel = 0
        
        if self.altitude == 0 and self.fuel == 0:
            self.active = False

        if self.active:
            self.time += dt

def display(sim):
    print('\033c')
    print(f'Speed: {int(sim.speed)}')
    print(f'Altitude: {int(sim.altitude)}')
    print(f'Fuel: {int(sim.fuel)}')
    print(f"Time: T+{sim.time:.1f}s")
        
sim = Simulation()
dt = 0.1
simspeed = 3

while True:
    sim.update(dt * simspeed)
    display(sim)
    time.sleep(dt)