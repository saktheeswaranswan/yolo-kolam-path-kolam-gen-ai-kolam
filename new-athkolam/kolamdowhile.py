import turtle
import math

class KolamLSystem:
    def __init__(self, axiom="FBFBFBFB", iterations=2, forward_len=10):
        self.axiom = axiom
        self.iterations = iterations
        self.forward_len = forward_len
        self.curve_colors = ["red", "blue", "green"]
        self.curve_index = 0
        self.instructions = ""

        self.t = turtle.Turtle()
        self.t.speed("fastest")
        self.t.pensize(2)

    def next_color(self):
        color = self.curve_colors[self.curve_index]
        self.curve_index = (self.curve_index + 1) % len(self.curve_colors)
        return color

    def generate_lsystem(self):
        current = self.axiom
        count = 0

        while True:  # do-while simulation for iterations
            next_str = ""
            i = 0

            while True:  # do-while simulation for character loop
                if i >= len(current):
                    break

                ch = current[i]
                if ch == 'A':
                    next_str += "AFBFA"
                elif ch == 'B':
                    next_str += "AFBFBFBFA"
                elif ch == 'F':
                    next_str += "F"
                else:
                    next_str += ch
                i += 1

            current = next_str
            count += 1
            if count >= self.iterations:
                break

        self.instructions = current

    def turtle_arc(self, radius, sweep_angle):
        self.t.pencolor(self.next_color())
        self.t.circle(radius, sweep_angle)

    def draw_lsystem(self):
        idx = 0

        while True:  # do-while simulation for drawing characters
            if idx >= len(self.instructions):
                break

            ch = self.instructions[idx]
            if ch == 'F':
                self.t.forward(self.forward_len)
            elif ch == 'A':
                self.turtle_arc(10, 90)
            elif ch == 'B':
                I = 5 / math.sqrt(2)
                self.t.forward(I)
                self.turtle_arc(I, 270)
                self.t.forward(I)
            idx += 1

    def setup_turtle(self):
        turtle.setup(800, 800)
        turtle.title("Kolam Pattern (OOP + do-while only)")
        turtle.bgcolor("white")
        self.t.penup()
        self.t.setpos(0, 0)
        self.t.pendown()

    def draw(self):
        self.setup_turtle()
        self.generate_lsystem()
        self.draw_lsystem()
        self.t.hideturtle()
        turtle.done()

# Create and run the Kolam drawing
kolam = KolamLSystem()
kolam.draw()

