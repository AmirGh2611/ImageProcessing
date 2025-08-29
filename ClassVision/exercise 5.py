import cv2
import numpy as np

# Global variables
points = []
current_color = (0, 255, 0)  # Default color is green


def draw_triangle(event, x, y, flags, param):
    global points, img, current_color

    # Left mouse click event
    if event == cv2.EVENT_LBUTTONDOWN:
        # Add the clicked point to our list
        points.append((x, y))

        # If we have 3 points, draw the triangle
        if len(points) == 3:
            # Convert points to numpy array
            triangle_cnt = np.array(points)

            # Draw the triangle with the current color
            cv2.drawContours(img, [triangle_cnt], 0, current_color, -1)

            # Reset points for next triangle
            points = []

            # Show the updated image
            cv2.imshow("Triangle Drawer", img)


# Create a black image (500x500)
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Create a window and set the mouse callback function
cv2.namedWindow("Triangle Drawer")
cv2.setMouseCallback("Triangle Drawer", draw_triangle)

# Display instructions
print("Click anywhere on the black image to create a triangle")
print("You need to click 3 times to define the triangle's vertices")
print("Press 'b' for blue triangles, 'r' for red, 'g' for green")
print("Press 'c' to clear the canvas")
print("Press 'ESC' to quit")

while True:
    # Display the image
    cv2.imshow("Triangle Drawer", img)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # Change color based on key press
    if key == ord('b'):  # Blue
        current_color = (255, 0, 0)
        print("Color changed to blue")
    elif key == ord('r'):  # Red
        current_color = (0, 0, 255)
        print("Color changed to red")
    elif key == ord('g'):  # Green
        current_color = (0, 255, 0)
        print("Color changed to green")
    elif key == ord('c'):  # Clear canvas
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        points = []
        print("Canvas cleared")
    elif key == 27:  # ESC key
        break

# Clean up
cv2.destroyAllWindows()