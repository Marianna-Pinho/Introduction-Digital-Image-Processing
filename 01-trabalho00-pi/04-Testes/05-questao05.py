import cv2 as cv
import numpy as np

#5 - Blending

img1 = cv.imread("images/baboon.png",0)
img2 = cv.imread("images/butterfly.png",0)

dst = cv.addWeighted(img1,0.8,img2,0.2,0)

cv.imshow('blending',dst)
cv.waitKey(0)
cv.destroyAllWindows()