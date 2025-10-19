# Exercise #4
# -----------
#
# Loading a video file and mirror it.

import numpy as np
import cv2

# TODO Just copy the code from exercise 3 and modify it to load a video file instead of the camera.
# Use the file "tutorials/data/videos/hello_UH.m4v" as input for the 'VideoCapture' function.

file = "./tutorials/data/videos/hello_UH.m4v"
cap = cv2.VideoCapture(file)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
print("Width: ", width)
print("Height: ", height)
print("Frame count : " + str(count))

# TODO Create a window for the video using 'namedWindow' with the title "Video image".
title ="Video image"
cv2.namedWindow(title, cv2.WINDOW_FREERATIO)
print("Press q to close the window.")

# TODO Start a loop to continuously read frames from the camera using 'while True:'.

while True:

# TODO (In loop) Read a camera frame with 'read' and check if that was successful.
    ret, frame = cap.read()
# TODO (In loop, if successful) (Skip this step for now and implement the display first in order 
# to see the camera image.)
    if ret:

# Create four flipped tiles of the image by first creating an empty image 
# with 'np.zeros'. Then resize the frame to half size using 'cv2.resize' with fx=0.5 and fy=0.5.
# Finally, fill in the four quadrants of the empty image with the original and flipped images
# using 'cv2.flip' with the appropriate flip codes (check the documentation).
        img = np.zeros(frame.shape, np.uint8)
        tile = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        img[0:tile.shape[0], 0:tile.shape[1]] = tile
        img[0:tile.shape[0], tile.shape[1]:] = cv2.flip(tile, 1)
        img[tile.shape[0]:, 0:tile.shape[1]] = cv2.flip(tile, 0)
        img[tile.shape[0]:, tile.shape[1]:] = cv2.flip(tile, -1)
# TODO (In loop, if successful) Display the image.
        cv2.imshow(title, img)
# TODO (In loop) Check if 'q' is pressed by comparing the return value of 'waitKey' with the 'ord'
# of the letter "q". Use simply 'break' to exit the loop.
    key = cv2.waitKey(20)
    if key == ord('q'):
        break


# TODO Release the video capture object with 'release' and close the window with 'destroyAllWindows'.
cap.release()
cv2.destroyAllWindows()