import cv2 as cv
import numpy as np

#3 - Slice bit planes

img = cv.imread('images/baboon.png',0)

n_bits = 8
planes = {}

for k in range(0,n_bits):
    planes[k] = ((img & 2**k) >> k)*255

cv.imshow('baboon',planes[7])
cv.waitKey(0)
cv.destroyAllWindows()