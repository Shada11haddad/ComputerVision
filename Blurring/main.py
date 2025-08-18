import os
import cv2


img = cv2.imread(os.path.join('.','img','deer.jpg'))


k_size = 7


blur_img= cv2.blur(img, (k_size, k_size))
Gaussian_blur_img= cv2.GaussianBlur(img, (k_size, k_size), 0)
median_blur_img= cv2.medianBlur(img,k_size)


# Display the blurred image
cv2.imshow('Gaussian Blur Image', Gaussian_blur_img)
cv2.imshow('median Blur Image', median_blur_img)
cv2.imshow('Blurred Image', blur_img)
cv2.imshow('Original Image', img)
cv2.waitKey(0)