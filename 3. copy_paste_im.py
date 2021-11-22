import cv2

img = cv2.imread('imgs/im.jpg', -1)

# Copy part of image
tag = img[200:400, 400:700]
img[100:300, 700:1000] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()