import numpy as np
import cv2
from ultralytics import YOLO  # pip install ultralytics needed

# load model (TODO:download one before running from https://github.com/ultralytics/assets/releases/)
# and adjust path accordingly
model = YOLO("./tutorials/data/models/yoloXXX.pt")

# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
focus = int(cap.get(cv2.CAP_PROP_AUTOFOCUS))

print('Video properties:')
print('  Width = ' + str(width))
print('  Height = ' + str(height))
print('  Codec = ' + str(codec))
print('  Autofocus = ' + str(focus))

title = 'Video image'
cv2.namedWindow(title, cv2.WINDOW_FREERATIO)  # Note that window parameters have no effect on MacOS
print('Press q to close the window.')

while True:
    ret, frame = cap.read()
    if (ret):
        # show the image
        img = frame.copy()
        # TODO detect objects in img
        # HINT use model.predict(source=img, stream=True, show=False)
        # and not this example: https://docs.ultralytics.com/modes/predict/#streaming-source-for-loop

        # TODO parse results and draw bounding boxes on img

        # show image with bounding boxes
        cv2.imshow(title, img)

        # press q to close the window
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not start video camera')
        break

cap.release()
cv2.destroyAllWindows()
