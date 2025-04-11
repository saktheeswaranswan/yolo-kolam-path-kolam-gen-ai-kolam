import random
import csv

# Square coordinates (corners)
corners = [(-150, -150), (150, -150), (150, 150), (-150, 150)]

# Generate random points inside the square
random_points = []
for _ in range(10):  # You can change 10 to the number of random points you want
    x = random.uniform(-150, 150)
    y = random.uniform(-150, 150)
    random_points.append((x, y))

# Combine square corners and random points
all_points = corners + random_points

# Export to CSV
with open("square_with_random_points.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y"])
    writer.writerows(all_points)

