import csv

# Parameters
side_length = 300
n = 10  # Points per side (including corners)
half = side_length // 2

# Square corners
corners = [
    (-half, -half),  # Bottom-left
    (half, -half),   # Bottom-right
    (half, half),    # Top-right
    (-half, half),   # Top-left
]

# Collect perimeter points
points = []

for i in range(4):
    x0, y0 = corners[i]
    x1, y1 = corners[(i + 1) % 4]
    for j in range(n):
        t = j / (n - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        points.append((x, y))

# Export CSV
with open("square_perimeter_points.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["x", "y"])
    writer.writerows(points)

