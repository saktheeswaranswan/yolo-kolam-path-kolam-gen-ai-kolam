import turtle
import math

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2      # Increase this to generate a more complex pattern
forward_len = 10    # Length for 'F'

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

def drawLSystem(instructions):
    """Interpret the L-system string and draw using turtle graphics."""
    for ch in instructions:
        if ch == 'F':
            turtle.forward(forward_len)
        elif ch == 'A':
            # Draw an arc with radius 10 and extent 90 degrees
            turtle.circle(10, 90)
        elif ch == 'B':
            # For symbol 'B', compute I = 5/sqrt(2),
            # then move forward by I, draw an arc of 270° with radius I, and move forward by I
            I = 5 / math.sqrt(2)
            turtle.forward(I)
            turtle.circle(I, 270)
            turtle.forward(I)

# Set up the turtle screen
turtle.setup(800, 800)
turtle.title("Single-Knot Kolam Pattern via L-System")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

# Optionally, set the starting position of the turtle
turtle.penup()
turtle.setpos(0, 0)  # You can adjust this if needed
turtle.pendown()

# Generate the L-system string
instructions = generateLSystem(axiom, iterations)

# Draw the Kolam pattern
drawLSystem(instructions)

# Hide the turtle and complete drawing
turtle.hideturtle()
turtle.done()

