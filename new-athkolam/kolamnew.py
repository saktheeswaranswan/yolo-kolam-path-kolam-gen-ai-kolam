import turtle
import math

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2      # Increase this to generate a more complex pattern
forward_len = 10    # Length for 'F'

# Colors to cycle through for each curve (arc)
curve_colors = ["red", "blue", "green"]
curve_index = 0

def next_color():
    """Return the next color in the cycle for drawing curves."""
    global curve_index
    col = curve_colors[curve_index]
    curve_index = (curve_index + 1) % len(curve_colors)
    return col

def generateLSystem(axiom, iter_count):
    """Generate the L-system string by applying rewriting rules."""
    current = axiom
    for _ in range(iter_count):
        next_str = ""
        for ch in current:
            if ch == 'A':
                next_str += "AFBFA"
            elif ch == 'B':
                next_str += "AFBFBFBFA"
            elif ch == 'F':
                next_str += "F"
            else:
                next_str += ch
        current = next_str
    return current

def turtleArc(r, sweepDeg):
    """
    Draw an arc with radius r and sweep angle sweepDeg.
    Sets the pen color to the next one in the cycle before drawing.
    """
    turtle.pencolor(next_color())
    turtle.circle(r, sweepDeg)

def drawLSystem(instructions):
    """Interpret the L-system string and draw using turtle graphics."""
    for ch in instructions:
        if ch == 'F':
            turtle.forward(forward_len)
        elif ch == 'A':
            # Draw an arc with radius 10 and sweep angle 90 degrees
            turtleArc(10, 90)
        elif ch == 'B':
            # For the symbol 'B': compute I = 5/sqrt(2),
            # then move forward by I, draw an arc of 270° with radius I, and move forward by I.
            I = 5 / math.sqrt(2)
            turtle.forward(I)
            turtleArc(I, 270)
            turtle.forward(I)

# --- Setup Turtle Screen ---
turtle.setup(800, 800)
turtle.title("Single-Knot Kolam Pattern via L-System")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

# Optionally set the starting position
turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()

# Generate the L-system instruction string
instructions = generateLSystem(axiom, iterations)

# Draw the Kolam pattern according to the L-system
drawLSystem(instructions)

# Hide the turtle and finish drawing
turtle.hideturtle()
turtle.done()

