import turtle
import math
import csv
import json

# Parameters
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
turtle.setup(1000, 1000)
turtle.title("Kolam Pattern on Square Boundary")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

instructions = generateLSystem(axiom, iterations)

# Square boundary
side_length = 400
half_side = side_length / 2
start_x, start_y = -half_side, -half_side

# Draw the square boundary
turtle.pencolor("black")
turtle.pensize(1)
turtle.penup()
turtle.setpos(start_x, start_y)
turtle.setheading(0)
turtle.pendown()
for _ in range(4):
    turtle.forward(side_length)
    turtle.left(90)
turtle.penup()

# Draw Kolam pattern along the square boundary
turtle.pensize(2)
turtle.pencolor(next_color())
turtle.setpos(start_x, start_y)
turtle.setheading(0)
turtle.pendown()
log_position("start_kolam")
for _ in range(4):
    drawLSystem(instructions)
    turtle.left(90)
log_position("end_kolam")
turtle.penup()

turtle.hideturtle()
export_data()
turtle.done()

