import cv2

img = cv2.imread(' imgs/im.jpg', -1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.dtype)
imgcopy = img.copy()

imgcopy = cv2.resize(imgcopy, (0, 0), fx=0.5, fy=0.5)
imgcopy = cv2.rotate(imgcopy, cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imwrite('new_img.jpg', imgcopy)

cv2.imshow('Image Copy', imgcopy)
cv2.waitKey(0)
cv2.destroyAllWindows()