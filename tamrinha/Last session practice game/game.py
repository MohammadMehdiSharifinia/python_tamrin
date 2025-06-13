import turtle
import random
import time

CELL_SIZE = 20
COLS = 40
ROWS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

class Cube:
    def __init__(self, x, y):
        self.t = turtle.Turtle()
        self.t.shape("square")
        self.t.color("red")
        self.t.penup()
        self.t.goto(x, y)
        self.alive = True

    def move_down(self):
        if self.alive:
            self.t.sety(self.t.ycor() - CELL_SIZE)

    def destroy(self):
        if self.alive:
            self.t.hideturtle()
            self.alive = False

class Bullet:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("triangle")
        self.t.color("green")
        self.t.penup()
        self.t.setheading(90)
        self.t.hideturtle()
        self.speed = 20
        self.active = False
        self.last_fire_time = 0
        self.cooldown = 1  # seconds

    def fire(self, x, y):
        current_time = time.time()
        if not self.active and current_time - self.last_fire_time >= self.cooldown:
            self.t.goto(x, y + 10)
            self.t.showturtle()
            self.active = True
            self.last_fire_time = current_time

    def move(self):
        if self.active:
            self.t.sety(self.t.ycor() + self.speed)
            if self.t.ycor() > HEIGHT // 2:
                self.reset()

    def reset(self):
        self.t.hideturtle()
        self.active = False

class Shooter:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("triangle")
        self.t.color("blue")
        self.t.penup()
        self.t.goto(0, -HEIGHT//2 + 20)
        self.t.setheading(90)

    def move_left(self):
        x = self.t.xcor() - CELL_SIZE
        if x > -WIDTH//2:
            self.t.setx(x)

    def move_right(self):
        x = self.t.xcor() + CELL_SIZE
        if x < WIDTH//2:
            self.t.setx(x)

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.cubes = []
        self.last_move_time = time.time()

        self.shooter = Shooter()
        self.bullet = Bullet()

        self.screen.listen()
        self.screen.onkeypress(self.shooter.move_left, "Left")
        self.screen.onkeypress(self.shooter.move_right, "Right")
        self.screen.onkeypress(lambda: self.bullet.fire(self.shooter.t.xcor(), self.shooter.t.ycor()), "space")

        self.spawn_cubes()

    def spawn_cubes(self):
        x_positions = random.sample(range(-WIDTH//2 + CELL_SIZE//2, WIDTH//2, CELL_SIZE), k=random.randint(5, 10))
        for x in x_positions:
            cube = Cube(x, HEIGHT//2 - CELL_SIZE//2)
            self.cubes.append(cube)

    def move_cubes_down(self):
        for cube in self.cubes:
            if cube.alive:
                cube.move_down()

    def check_collisions(self):
        if not self.bullet.active:
            return
        for cube in self.cubes:
            if cube.alive and self.bullet.t.distance(cube.t) < CELL_SIZE:
                cube.destroy()
                self.bullet.reset()
                return

    def run(self):
        while True:
            self.screen.update()

            self.bullet.move()
            self.check_collisions()

            if time.time() - self.last_move_time > 5:
                self.move_cubes_down()
                self.spawn_cubes()
                self.last_move_time = time.time()

game = Game()
game.run()
