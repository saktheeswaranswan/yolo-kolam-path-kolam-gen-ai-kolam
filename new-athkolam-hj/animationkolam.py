import turtle
import math
import csv
import json

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2
forward_len = 10
curve_colors = ["red", "blue", "green"]
curve_index = 0
movement_log = []

current_time_ms = 0  # Starts at 0 ms
time_step_ms = 50    # Time increment per movement step

def next_color():
    global curve_index
    col = curve_colors[curve_index]
    curve_index = (curve_index + 1) % len(curve_colors)
    return col

def log_position(action):
    """Log turtle position with manual animation time counter."""
    global current_time_ms
    x, y = turtle.pos()
    movement_log.append({
        "time_ms": current_time_ms,
        "x": x,
        "y": y,
        "action": action
    })
    current_time_ms += time_step_ms  # Increment after each movement step

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
            turtleArc(10, 90)
        elif ch == 'B':
            I = 5 / math.sqrt(2)
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
turtle.title("Single-Knot Kolam Pattern via L-System")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()

log_position("start")

instructions = generateLSystem(axiom, iterations)
drawLSystem(instructions)

turtle.hideturtle()
export_data()
turtle.done()

