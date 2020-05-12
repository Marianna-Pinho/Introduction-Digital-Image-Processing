import cv2 as cv
import numpy as np

#reading image
img = cv.imread('../images/city.png')

#i) Computes the negative of the image
dst = cv.bitwise_not(img)

#ii) Changes image intesity to [100,200] interval
#img = cv.convertScaleAbs(img,alpha=100/255,beta=100)
dst = np.floor((100/255)*img + 100).astype(np.uint8)

#iii) Invert (flip) even lines (is this vectorized???)
img[::2] = cv.flip(img[::2],1)
dst = img

#iv) Mirror the top of the image at the bottom
middle = img.shape[0]//2
img_m = cv.flip(img[:middle],0)
img[middle:] = img_m

dst = img

cv.imshow('city',dst)
cv.waitKey(0)
cv.destroyAllWindows()