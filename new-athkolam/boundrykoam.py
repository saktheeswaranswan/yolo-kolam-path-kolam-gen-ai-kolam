import turtle
import math
import csv
import json

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2
forward_len = 3.5
curve_colors = ["red", "blue", "green"]
curve_index = 0
movement_log = []

current_time_ms = 0
time_step_ms = 50

def next_color():
    global curve_index
    col = curve_colors[curve_index]
    curve_index = (curve_index + 1) % len(curve_colors)
    return col

def log_position(action):
    global current_time_ms
    x, y = turtle.pos()
    movement_log.append({
        "time_ms": current_time_ms,
        "x": round(x, 3),
        "y": round(y, 3),
        "action": action
    })
    current_time_ms += time_step_ms

def generateLSystem(axiom, iter_count):
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
    turtle.pencolor(next_color())
    steps = int(abs(sweepDeg) / 5)
    for _ in range(steps):
        turtle.circle(r, sweepDeg / steps)
        log_position("arc")

def drawLSystem(instructions):
    for ch in instructions:
        if ch == 'F':
            turtle.forward(forward_len)
            log_position("forward")
        elif ch == 'A':
            turtleArc(3.5, 90)
        elif ch == 'B':
            I = 1.75 / math.sqrt(2)
            turtle.forward(I)
            log_position("forward-B-start")
            turtleArc(I, 270)
            turtle.forward(I)
            log_position("forward-B-end")

def export_data():
    with open("kolam_coords.json", "w") as jf:
        json.dump(movement_log, jf, indent=4)

    with open("kolam_coords.csv", "w", newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=["time_ms", "x", "y", "action"])
        writer.writeheader()
        writer.writerows(movement_log)

# --- Turtle Setup ---
turtle.setup(800, 800)
turtle.title("Symmetric Rhombus Kolam Pattern")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

# Generate full instruction string
instructions = generateLSystem(axiom, iterations)

# Draw pattern 4 times (each side of rhombus)
for i in range(4):
    angle = 45 + i * 90
    turtle.penup()
    # Move to center and rotate outward
    radius = 2.5
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    turtle.setpos(x, y)
    turtle.setheading(angle)
    turtle.pendown()
    log_position(f"start_loop_{i+1}")
    drawLSystem(instructions)
    turtle.penup()
    log_position(f"end_loop_{i+1}")

# Optional: Draw bounding circle
turtle.setpos(0, -5)
turtle.setheading(0)
turtle.pencolor("black")
turtle.pendown()
turtle.circle(5)
turtle.penup()

turtle.hideturtle()
export_data()
turtle.done()

