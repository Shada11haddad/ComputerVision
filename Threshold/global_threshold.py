import os
import cv2

img = cv2.imread(os.path.join('.', 'img', 'deer.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold(img_gray, 80, 255 , cv2.THRESH_BINARY)
cv2.imshow('Original Image', img)
cv2.imshow('gray Image', img_gray)
cv2.imshow('thresh Image', thresh)
cv2.waitKey(0)