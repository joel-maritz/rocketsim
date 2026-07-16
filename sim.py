class Simulation:
    def __init__(self):
        self.engine_on = False
        self.throttle = 0.0
        self.fuel = 200
        self.fuelDecay = 5
        self.speed = 0
        self.altitude = 0
        self.gravity = 9.81
        self.maxthrust = 20
        self.weight = 1000
        self.maxSpeed = 1200 - self.weight
        self.time = 0
        self.active = True
    def update(self, dt):
        if self.engine_on and self.fuel > 0:
            current_thrust = self.maxthrust * self.throttle
            self.speed += current_thrust * dt
            self.fuel -= self.fuelDecay * dt
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