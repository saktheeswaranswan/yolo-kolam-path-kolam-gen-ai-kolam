import turtle
import math
import time
import csv
import json

# L-system parameters
axiom = "FBFBFBFB"
iterations = 2
forward_len = 10
curve_colors = ["red", "blue", "green"]
curve_index = 0
movement_log = []

def next_color():
    global curve_index
    col = curve_colors[curve_index]
    curve_index = (curve_index + 1) % len(curve_colors)
    return col

def log_position(action):
    x, y = turtle.pos()
    timestamp_raw = time.time()
    timestamp_str = time.strftime("%a, %I:%M %p, %B %d, %Y", time.localtime(timestamp_raw))
    movement_log.append({
        "timestamp_raw": timestamp_raw,
        "timestamp_str": timestamp_str,
        "x": x,
        "y": y,
        "action": action
    })

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
        writer = csv.DictWriter(cf, fieldnames=["timestamp_raw", "timestamp_str", "x", "y", "action"])
        writer.writeheader()
        writer.writerows(movement_log)

def read_points_from_csv(file_path):
    points = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x = float(row['x'])
            y = float(row['y'])
            points.append((x, y))
    return points

# --- Turtle Setup ---
turtle.setup(1000, 1000)
turtle.title("Kolam Islands at CSV Points")
turtle.bgcolor("white")
turtle.speed("fastest")
turtle.pensize(2)

# Generate L-system instructions once
instructions = generateLSystem(axiom, iterations)

# Read center points from CSV
points = read_points_from_csv("square_with_random_points.csv")

# Draw Kolam island at each center point
for idx, (cx, cy) in enumerate(points):
    turtle.penup()
    turtle.goto(cx, cy)
    log_position(f"center-island-{idx+1}")
    turtle.setheading(0)
    turtle.pendown()
    
    # Draw full cycle of L-system (like an island)
    drawLSystem(instructions)

    turtle.penup()
    turtle.goto(cx, cy)  # Return to center to finish
    turtle.pendown()

turtle.hideturtle()
export_data()
turtle.done()

