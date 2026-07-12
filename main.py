import time
class Sim:
    def __init__(self):
        self.fuel = 500
        self.fuelDecayRate = 5

        self.speed = 0
        self.altitude = 0

        self.thrust = 50
        self.gravity = 9.81

        self.maxSpeed = 200

    def update(self):
        print('\033c')

        if self.fuel > 0:
            self.speed += self.thrust
            self.fuel -= self.fuelDecayRate

        self.speed -= self.gravity

        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed

        self.altitude += self.speed

        if self.altitude < 0:
            self.altitude = 0
            self.speed = 0

        print(f'Speed: {int(self.speed)}')
        print(f'Altitude: {int(self.altitude)}')
        print(f'Fuel: {int(self.fuel)}')
        
sim = Sim()

while True:
    sim.update()
    time.sleep(0.1)