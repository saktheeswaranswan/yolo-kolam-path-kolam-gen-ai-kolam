import turtle
import math

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2
forward_len = 20  # Base forward movement

# Colors to cycle through
curve_colors = ["red", "blue", "green"]
curve_index = 0

def next_color():
    """Cycle through colors for curve drawing."""
    global curve_index
    color = curve_colors[curve_index]
    curve_index = (curve_index + 1) % len(curve_colors)
    return color

def generateLSystem(axiom, iter_count):
    """Apply L-system rules to generate pattern."""
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

def turtleArc(radius, angle):
    """Draw a colored arc."""
    turtle.pencolor(next_color())
    turtle.circle(radius, angle)

def drawLSystem(instructions):
    """Interpret and draw the L-system with square boundary orientation."""
    for ch in instructions:
        if ch == 'F':
            turtle.forward(forward_len)
        elif ch == 'A':
            # 90-degree arc (outward bulge on square side)
            turtleArc(10, 90)
        elif ch == 'B':
            # Corner curve (like bending around square corner)
            I = 5 / math.sqrt(2)
            turtle.forward(I)
            turtleArc(I, 270)
            turtle.forward(I)
            turtle.left(90)  # Turn to align with next square edge

# --- Turtle setup ---
turtle.setup(800, 800)
turtle.title("Kolam Around Square Boundary")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

# Center the pattern
turtle.penup()
turtle.setpos(-100, -100)  # Adjust to center
turtle.setheading(0)       # Face right (east)
turtle.pendown()

# Generate and draw
lsystem_string = generateLSystem(axiom, iterations)
drawLSystem(lsystem_string)

# Finish
turtle.hideturtle()
turtle.done()

