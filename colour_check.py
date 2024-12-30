import cv2
from math import sqrt

# Define a dictionary of common colors and their RGB values
COLORS = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Gray": (128, 128, 128),
    "Orange": (255, 165, 0),
    "Pink": (255, 192, 203),
    "Brown": (165, 42, 42),
    "Purple": (128, 0, 128),
}

def get_rgb_from_frame(frame, center_x, center_y, radius):
    # Extract the BGR value of the pixel at the center
    b, g, r = frame[center_y, center_x]
    return (r, g, b)

def get_closest_color_name(rgb):
    closest_color = None
    min_distance = float("inf")

    for color_name, color_rgb in COLORS.items():
        # Calculate the Euclidean distance between the RGB values
        distance = sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(rgb, color_rgb)))
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name

    return closest_color

# Open the camera
cap = cv2.VideoCapture(0)  # 0 for the default camera, change if using another camera

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 'q' to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Flip the frame horizontally for a natural mirrored view
    frame = cv2.flip(frame, 1)

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Calculate the center of the frame
    center_x, center_y = width // 2, height // 2
    radius = 20  # Radius of the circle

    # Draw a circle at the center of the frame
    cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)

    # Get RGB value from the center of the circle
    rgb_value = get_rgb_from_frame(frame, center_x, center_y, radius)

    # Get the closest color name
    color_name = get_closest_color_name(rgb_value)

    # Print RGB value and color name in the terminal
    print(f"RGB Value: {rgb_value}, Color Name: {color_name}")

    # Display the frame
    cv2.imshow("Camera - RGB Detector with Color Name", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
