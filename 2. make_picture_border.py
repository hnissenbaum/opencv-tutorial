import cv2
import random

img = cv2.imread('imgs/im.jpg', -1)

# Change border to random pixels

#top border
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#left border
for i in range(img.shape[0]):    
    for j in range(100):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#right border
for i in range(img.shape[1]-100, (img.shape[1])):    
    for j in range(img.shape[0]):
        img[j][i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#bottom border
for i in range(img.shape[0]-100, (img.shape[0])):    
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()