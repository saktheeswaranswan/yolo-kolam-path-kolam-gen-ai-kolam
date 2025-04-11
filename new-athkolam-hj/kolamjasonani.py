import turtle
import math
import csv
import json
import time

# --- L-System Parameters ---
axiom = "FBFBFBFB"
iterations = 2
forward_len = 10

# --- Data Storage ---
path_points = []

# --- Color Management ---
colors = ["red", "blue", "green", "orange", "purple", "teal", "magenta", "brown"]
color_index = 0

def next_color():
    global color_index
    col = colors[color_index]
    color_index = (color_index + 1) % len(colors)
    turtle.pencolor(col)

# --- L-System Generator ---
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

# --- Position Recorder ---
def record_position():
    x, y = turtle.pos()
    timestamp = time.time()
    path_points.append({
        "x": round(x, 2),
        "y": round(y, 2),
        "timestamp": timestamp
    })

# --- Drawing Functions ---
def drawArc(radius, angle, tilt=45):
    turtle.left(tilt)
    for _ in range(int(angle)):
        turtle.circle(radius, 1)
        record_position()
        time.sleep(0.001)  # Creates animated effect
    turtle.right(tilt)

def drawLSystem(instructions):
    for ch in instructions:
        if ch == 'F':
            turtle.forward(forward_len)
            record_position()
            time.sleep(0.01)
        elif ch == 'A':
            next_color()
            drawArc(10, 90, tilt=45)
        elif ch == 'B':
            next_color()
            I = 5 / math.sqrt(2)
            turtle.forward(I)
            record_position()
            drawArc(I, 270, tilt=45)
            turtle.forward(I)
            record_position()

# --- Turtle Setup ---
def setupTurtle():
    turtle.setup(800, 800)
    turtle.title("Animated Rhomboid Kolam with JSON/CSV Export")
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.pensize(2)
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.setheading(45)
    turtle.pendown()
    record_position()

# --- CSV Export ---
def export_to_csv(filename="boundary_points.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y", "timestamp"])
        for point in path_points:
            writer.writerow([point["x"], point["y"], point["timestamp"]])
    print(f"Exported {len(path_points)} points to {filename}")

# --- JSON Export ---
def export_to_json(filename="boundary_points.json"):
    with open(filename, 'w') as file:
        json.dump(path_points, file, indent=4)
    print(f"Exported {len(path_points)} points to {filename}")

# --- Main Execution ---
setupTurtle()
instructions = generateLSystem(axiom, iterations)
drawLSystem(instructions)
turtle.hideturtle()
turtle.done()

# --- Export the path data ---
export_to_csv()
export_to_json()

