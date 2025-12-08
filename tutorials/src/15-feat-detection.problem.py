# Exercise #15
# ------------
#
# Compute the features of an image with the Harris corner detection. Adjust the parameters using sliders.

import numpy as np
import cv2

# TODO Define a function that detects and draws corners into the image
def draw_features(corners):
# Drawing helper variables
    thick = 5
    thin = 2
    filled = -1

    small_size = 3
    medium_size = 5
    large_size = 7
# Get a different color array for each of the features/corners
    colors = np.random.uiform(0,255, size=(len(corners), 3))
# Draw a circle around each corner
    img = np.copy(img_clone)
# Show the resulting image
    for corner, color in zip(corners, colors):

        cv2.circle(img, tuple(corner.ravel()), medium_size, color, thin)

# TODO Define the callback function
# Read paremeters from slider positions
def on_change(val):
# Run corner detection
    max_number_of_features = cv2.getTrackbarPos("max_number_of_features", window_name)
    min_quality_trackbar_value = cv2.getTrackbarPos("min_quality", window_name)
    min_quality = min_quality_trackbar_value / 10
    min_euclid_dist = cv2.getTrackbarPos("min_euclid_dist", window_name)

    corners = cv2.goodFeaturesToTrack(img_gray,
                                      max_number_of_features,
                                      min_quality,
                                      min_euclid_dist,
                                      useHarrisDetector=True)
    
    corners = np.intp(corners)
    draw_features(corners)

# cv2.goodFeaturesToTrack returns corners as floating point values,
# hence convert to integer

# Call the function from above to draw the corners into the image

# TODO Load example image as color image
img = cv2.imread("./tutorials/data/images/logo.png", cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400))

# TODO Clone image
img_clone = np.copy(img)

# TODO Create a greyscale image for the corner detection
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# TODO Create a window with sliders and show resulting image
window_name = "Good features demo"
cv2.imshow(window_name, img)

# TODO Create sliders for all parameters and one callback function
cv2.createTrackbar("max_number_of_features", window_name, 10, 500, on_change)
cv2.createTrackbar("min_quality", window_name, 3, 10, on_change)
cv2.createTrackbar("min_euclid_dist", window_name, 15, 100, on_change)

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
