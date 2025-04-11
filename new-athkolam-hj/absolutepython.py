import cv2
import numpy as np
import time

# Set up webcam capture (0 is the default webcam)
cap = cv2.VideoCapture(0)

# Initial coordinates for the square (points from (0, 0) to (10, 10))
square_points = [(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]  # Square path
current_position = square_points[0]  # Start at (0, 0)
current_point_index = 0
line_coordinates = []

# Scaling factors
scale_factor = 1  # Initial scale factor (normal size)

# Function to scale the square
def scale_square(points, scale_factor):
    return [(x * scale_factor, y * scale_factor) for x, y in points]

# Function to show webcam feed with the overlaid square trace
def show_webcam_with_square_trace():
    global square_points, scale_factor, current_position, current_point_index, line_coordinates
    last_update_time = time.time()
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break
        
        # Draw the square on the webcam frame using OpenCV
        for i in range(len(square_points) - 1):
            pt1 = (int(square_points[i][0]), int(square_points[i][1]))
            pt2 = (int(square_points[i + 1][0]), int(square_points[i + 1][1]))
            cv2.line(frame, pt1, pt2, (255, 0, 0), 2)  # Blue color square

        # Draw the animated line (from one point to the next)
        if len(line_coordinates) > 1:
            cv2.line(frame, line_coordinates[-2], line_coordinates[-1], (0, 255, 0), 2)  # Green color line

        # Display the coordinates of the corners of the square
        for i, point in enumerate(square_points[:-1]):
            text = f"({int(point[0])}, {int(point[1])})"
            cv2.putText(frame, text, (int(point[0]) + 5, int(point[1]) - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        # Display the current position of the line
        cv2.putText(frame, f"Moving to: {square_points[current_point_index]}", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Display the webcam feed in a window
        cv2.imshow("Webcam Feed with Square", frame)

        # Key press event to control the square and scale
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Press 'Q' to quit
            break
        elif key == ord('s'):  # Scale down
            scale_factor *= 0.5
            square_points = scale_square([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)], scale_factor)
            print(f"Square scaled down by a factor of 0.5. New scale factor: {scale_factor}")
        elif key == ord('b'):  # Scale up
            scale_factor *= 2
            square_points = scale_square([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)], scale_factor)
            print(f"Square scaled up by a factor of 2. New scale factor: {scale_factor}")

        # Animation effect: Control animation speed
        current_time = time.time()
        if current_time - last_update_time >= 0.05:  # Update position every 50ms
            last_update_time = current_time
            
            if len(line_coordinates) == 0:
                line_coordinates.append(square_points[0])  # Start from the first point
                
            if current_point_index < len(square_points) - 1:
                line_coordinates.append(square_points[current_point_index])
                current_point_index += 1
            else:
                # When the animation reaches the last point, stop or reset
                print("Animation complete. Resetting.")
                current_point_index = 0
                line_coordinates = []

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

# Start the function to show webcam with square trace
show_webcam_with_square_trace()

