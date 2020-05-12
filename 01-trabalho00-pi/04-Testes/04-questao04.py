import cv2 as cv
import numpy as np

#4 - Mosaic

img = cv.imread("images/baboon.png",0)

n_cols,n_lines = img.shape
n_slices = 4
n_cols_slice = n_cols//4 
n_lines_slice = n_lines//4
pattern = [6,11,13,3,8,16,1,9,12,14,2,7,4,15,10,5]

img_slices = {}
mosaic = np.zeros(shape=(n_cols, n_lines),dtype=np.uint8)

pos = 0
for col_pos in range(0,n_slices):
    for line_pos in range(0,n_slices):
        img_slices[pos] = img[col_pos*n_cols_slice:n_cols_slice*(1 + col_pos), line_pos*n_lines_slice:n_lines_slice*(1 + line_pos)]
        pos = pos+1

pos = 0
for col_pos in range(0,n_slices):
    for line_pos in range(0,n_slices):
        mosaic[col_pos*n_cols_slice:n_cols_slice*(1 + col_pos), \
            line_pos*n_lines_slice:n_lines_slice*(1 + line_pos)] = img_slices[pattern[pos]-1]
        pos = pos + 1
        
cv.imshow('baboon',mosaic)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('mosaic.png',mosaic)