import turtle
import random
import time
import math

class Shape:
    def __init__(self, shape_type, max_health, speed, defeats, color, stretch):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        
        self.shape_type = shape_type
        self.health = max_health
        self.speed = speed
        self.defeats = defeats      # لیست shape_typeهایی که این شکل می‌تواند بزند
        self.stretch = stretch      # (stretch_len, stretch_wid, outline)
        
        # ظاهر
        self.turtle.shape("circle")
        self.turtle.shapesize(*stretch)
        self.turtle.color(color)
        
        # جهت و سرعت تصادفی
        angle = random.uniform(0, 360)
        rad = math.radians(angle)
        self.dx = math.cos(rad) * speed
        self.dy = math.sin(rad) * speed

    def move(self):
        self.turtle.goto(self.turtle.xcor() + self.dx,
                         self.turtle.ycor() + self.dy)

    def bounce(self):
        w = turtle.window_width()  // 2 - 20
        h = turtle.window_height() // 2 - 20
        if abs(self.turtle.xcor()) > w:
            self.dx *= -1
        if abs(self.turtle.ycor()) > h:
            self.dy *= -1

    def is_collision(self, other):
        dist = self.turtle.distance(other.turtle.pos())
        thresh = (self.stretch[0] + other.stretch[0]) * 10
        return dist < thresh


class Square(Shape):
    def __init__(self):
        super().__init__(
            shape_type='q',
            max_health=4,
            speed=2,
            defeats=['n'],       # مربع دایره را می‌زند
            color='red',
            stretch=(1.5,1.5,1)
        )
        self.turtle.shape("square")


class Triangle(Shape):
    def __init__(self):
        super().__init__(
            shape_type='p',
            max_health=3,
            speed=2.5,
            defeats=['n'],       # مثلث دایره را می‌زند
            color='green',
            stretch=(1.3,1.3,1)
        )
        self.turtle.shape("triangle")


class Rectangle(Shape):
    def __init__(self):
        super().__init__(
            shape_type='m',
            max_health=5,
            speed=1.8,
            defeats=['q'],       # مستطیل مربع را می‌زند
            color='blue',
            stretch=(2.0,1.0,1)
        )
        # چون "rectangle" در turtle نیست، از "square" کشیده استفاده می‌کنیم
        self.turtle.shape("square")


class Circle(Shape):
    def __init__(self):
        super().__init__(
            shape_type='n',
            max_health=6,
            speed=2.2,
            defeats=['m'],       # دایره مستطیل را می‌زند
            color='yellow',
            stretch=(1.0,1.0,1)
        )
        self.turtle.shape("circle")


class Game:
    def __init__(self):
        self.shapes = []
        self.setup_screen()
        self.create_shapes()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("بازی شکل‌ها")
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("white")
        self.screen.tracer(0)

    def create_shapes(self):
        for cls in (Square, Triangle, Rectangle, Circle):
            for _ in range(random.randint(3, 7)):
                s = cls()
                s.turtle.goto(random.randint(-350, 350),
                              random.randint(-250, 250))
                self.shapes.append(s)

    def handle_collisions(self):
        to_remove = set()
        for i in range(len(self.shapes)):
            for j in range(i+1, len(self.shapes)):
                a = self.shapes[i]
                b = self.shapes[j]
                if a.is_collision(b):
                    # اگر a بتواند b را بزند
                    if b.shape_type in a.defeats:
                        b.health -= 1
                    # اگر b بتواند a را بزند
                    elif a.shape_type in b.defeats:
                        a.health -= 1
                    # برخورد خنثی: فقط معکوس جهت
                    # (بدون کاهش جان)

                    # معکوس کردن جهت پس از برخورد
                    a.dx, a.dy = -a.dx, -a.dy
                    b.dx, b.dy = -b.dx, -b.dy

                    # حذف هر شکل با health صفر
                    if a.health <= 0:
                        to_remove.add(a)
                    if b.health <= 0:
                        to_remove.add(b)

        for shp in to_remove:
            shp.turtle.hideturtle()
            if shp in self.shapes:
                self.shapes.remove(shp)

    def run(self):
        try:
            while self.shapes:
                self.screen.update()
                for s in self.shapes:
                    s.move()
                    s.bounce()
                self.handle_collisions()
                time.sleep(0.01)
            print("بازی پایان یافت!")
        except turtle.Terminator:
            pass
        finally:
            turtle.bye()


if __name__ == "__main__":
    Game().run()
