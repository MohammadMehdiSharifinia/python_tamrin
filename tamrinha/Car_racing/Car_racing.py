import random

class Engine:
    def __init__(self):
        self.fuel_usage = random.uniform(0.08, 0.12)
        self.top_speed = random.randint(150, 210)

class FuelTank:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.level = capacity

    def consume(self, amount):
        self.level = max(0, self.level - amount)

    def refill(self):
        self.level = self.capacity

class Position:
    def __init__(self, start=0):
        self.value = start

    def move(self, distance):
        self.value += distance

class GasStation:
    def __init__(self, location, capacity=4):
        self.location = location
        self.capacity = capacity
        self.queue = []

    def has_space(self):
        return len(self.queue) < self.capacity

    def enter(self, car):
        if self.has_space():
            self.queue.append(car)

    def exit(self, car):
        if car in self.queue:
            self.queue.remove(car)

class Vehicle:
    def __init__(self, color, start_pos):
        self.color = color
        self.engine = Engine()
        self.tank = FuelTank()
        self.position = Position(start_pos)
        self.time = 0
        self.status = "moving"
        self.refuel_delay = random.randint(3, 7)
        self.assigned_station = None

    def proceed(self, dt, stations):
        if self.status == "moving":
            self._move(dt)
            if self.tank.level <= 0:
                self._seek_station(stations)
        elif self.status == "refueling":
            self._refuel(dt)
        elif self.status == "waiting":
            self._check_station()

    def _move(self, dt):
        dist_possible = self.engine.top_speed * dt
        fuel_limit = self.tank.level / self.engine.fuel_usage
        dist = min(dist_possible, fuel_limit)
        self.position.move(dist)
        self.tank.consume(dist * self.engine.fuel_usage)
        self.time += dt
        if self.tank.level <= 0:
            self.status = "seek_station"

    def _seek_station(self, stations):
        nearest = min(stations, key=lambda s: abs(s.location - self.position.value))
        if nearest.has_space():
            nearest.enter(self)
            self.assigned_station = nearest
            self.status = "refueling"
        else:
            self.status = "waiting"
            self.assigned_station = nearest

    def _refuel(self, dt):
        self.refuel_delay -= dt
        self.time += dt
        if self.refuel_delay <= 0:
            self.tank.refill()
            self.status = "moving"
            self.refuel_delay = random.randint(3, 7)
            if self.assigned_station:
                self.assigned_station.exit(self)
                self.assigned_station = None

    def _check_station(self):
        if self.assigned_station and self.assigned_station.has_space():
            self.assigned_station.enter(self)
            self.status = "refueling"

    def is_done(self, goal):
        return self.position.value >= goal

def setup_cars():
    palette = ["قرمز", "آبی", "سبز"]
    cars = []
    last_pos = 0
    for color in palette:
        start = last_pos + random.randint(500, 700)
        cars.append(Vehicle(color, start))
        last_pos = start
    return cars

def setup_stations():
    return [GasStation(random.randint(0, 10000)) for _ in range(3)]

def simulate_race():
    finish_line = 10000
    dt = 1
    cars = setup_cars()
    stations = setup_stations()
    completed = []

    while len(completed) < len(cars):
        for car in cars:
            if car.is_done(finish_line):
                if car not in completed:
                    completed.append(car)
            else:
                car.proceed(dt, stations)

    champ = min(completed, key=lambda c: c.time)
    print(f"🏁 ماشین {champ.color} برنده شد با زمان {round(champ.time, 2)} ثانیه")

if __name__ == "__main__":
    simulate_race()
