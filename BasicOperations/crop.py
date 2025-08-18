import os
import cv2


img = cv2.imread(os.path.join('.', 'data', 'Coyote.jpeg'))
print(img.shape)
corpped_img = img[10:50, 20:50]
cv2.imshow('corpped_img', corpped_img)
cv2.imshow('img',img)
cv2.waitKey(0)