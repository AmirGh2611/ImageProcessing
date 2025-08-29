import cv2
import numpy as np

# Global variables
drawing = False
last_x, last_y = -1, -1
pen_size = 3
pen_color = (0, 255, 0)  # Default color is green

# Create a black image (500x500)
img = np.zeros((500, 500, 3), dtype=np.uint8)


# Mouse callback function
def draw_line(event, x, y, flags, param):
    global drawing, last_x, last_y, img, pen_size, pen_color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y
        # Draw a circle at the starting point
        cv2.circle(img, (x, y), pen_size, pen_color, -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Draw a line from the last point to the current point
            cv2.line(img, (last_x, last_y), (x, y), pen_color, pen_size)
            last_x, last_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Draw a final line to the endpoint
        cv2.line(img, (last_x, last_y), (x, y), pen_color, pen_size)


# Trackbar callback functions
def update_pen_size(val):
    global pen_size
    pen_size = val


def update_blue(val):
    global pen_color
    pen_color = (val, pen_color[1], pen_color[2])


def update_green(val):
    global pen_color
    pen_color = (pen_color[0], val, pen_color[2])


def update_red(val):
    global pen_color
    pen_color = (pen_color[0], pen_color[1], val)


# Create window and trackbars
cv2.namedWindow("Paint Program")
cv2.createTrackbar("Pen Size", "Paint Program", pen_size, 5, update_pen_size)
cv2.createTrackbar("Blue", "Paint Program", pen_color[0], 255, update_blue)
cv2.createTrackbar("Green", "Paint Program", pen_color[1], 255, update_green)
cv2.createTrackbar("Red", "Paint Program", pen_color[2], 255, update_red)

# Set mouse callback
cv2.setMouseCallback("Paint Program", draw_line)

# Display instructions
print("Simple Paint Program")
print("1. Hold left mouse button to draw")
print("2. Adjust pen size with the 'Pen Size' trackbar (1-5)")
print("3. Adjust colors with the Blue, Green, and Red trackbars")
print("4. Press 'c' to clear the canvas")
print("5. Press 'ESC' to quit")

while True:
    # Display the image
    cv2.imshow("Paint Program", img)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):  # Clear canvas
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        print("Canvas cleared")
    elif key == 27:  # ESC key
        break

# Clean up
cv2.destroyAllWindows()