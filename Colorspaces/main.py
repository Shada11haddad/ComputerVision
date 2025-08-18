import os 
import cv2

img = cv2.imread(os.path.join('.','img','butterfly.jpg'))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)
print(f"gray image channel :{img_gray.shape}")
print(f"hsv image channel :{img_hsv.shape}")

cv2.waitKey(0)