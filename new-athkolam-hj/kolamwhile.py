import turtle
import math

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2
forward_len = 10

# Colors for arcs
curve_colors = ["red", "blue", "green"]
curve_index = 0

def next_color():
    """Cycle through curve colors."""
    global curve_index
    col = curve_colors[curve_index]
    curve_index = (curve_index + 1) % len(curve_colors)
    return col

def generateLSystem(axiom, iter_count):
    """Generate L-system string using while loop."""
    current = axiom
    count = 0
    while count < iter_count:
        next_str = ""
        i = 0
        while i < len(current):
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
    return current

def turtleArc(r, sweepDeg):
    """Draw an arc with the next color."""
    turtle.pencolor(next_color())
    turtle.circle(r, sweepDeg)

def drawLSystem(instructions):
    """Interpret and draw L-system using while loop."""
    index = 0
    while index < len(instructions):
        ch = instructions[index]
        if ch == 'F':
            turtle.forward(forward_len)
        elif ch == 'A':
            turtleArc(10, 90)
        elif ch == 'B':
            I = 5 / math.sqrt(2)
            turtle.forward(I)
            turtleArc(I, 270)
            turtle.forward(I)
        index += 1

# --- Setup Turtle ---
turtle.setup(800, 800)
turtle.title("Single-Knot Kolam Pattern via L-System")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

# Move to starting position
turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()

# Generate instructions and draw
instructions = generateLSystem(axiom, iterations)
drawLSystem(instructions)

# Finish
turtle.hideturtle()
turtle.done()

