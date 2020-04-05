# import cv2
# import numpy as np

# ## Read
# img = cv2.imread("rgb.jpg")

# ## convert to hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ## mask of green (36,25,25) ~ (86, 255,255)
# # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
# # mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
# mask = cv2.inRange(hsv, (45,100,70), (75, 255,255))

# ## slice the green
# imask = mask>0
# green = np.zeros_like(img, np.uint8)
# green[imask] = img[imask]

# ## save 
# cv2.imwrite("grn_test.jpg", green)



import cv2
import numpy as np

img = cv2.imread('rgb.jpg')

ORANGE_MIN = np.array([45,100,70],np.uint8)
ORANGE_MAX = np.array([75, 255,255],np.uint8)

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
cv2.imwrite('output2.jpg', frame_threshed)