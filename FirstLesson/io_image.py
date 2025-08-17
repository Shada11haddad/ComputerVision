import os
import cv2

# Build the path for input image
image_path = os.path.join('.', 'data', 'Coyote.jpeg')

# Read the image
img = cv2.imread(image_path)

cv2.imwrite(os.path.join('.', 'data', 'Coyote_out.jpeg'), img)


cv2.imshow('Image', img)
cv2.waitKey(0)