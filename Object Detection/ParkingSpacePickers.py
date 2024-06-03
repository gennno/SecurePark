import cv2
import pickle

# Dimensions of the rectangles
width, height = 65, 110

# Try to load existing positions from file, otherwise start with an empty list
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

# Function to handle mouse clicks
def mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                break

    # Save the updated list to the file
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    # Read the image
    img = cv2.imread('Parkir1.png')

    # Draw rectangles on the image
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    # Display the image with the rectangles
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouse_click)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy all OpenCV windows
cv2.destroyAllWindows()
