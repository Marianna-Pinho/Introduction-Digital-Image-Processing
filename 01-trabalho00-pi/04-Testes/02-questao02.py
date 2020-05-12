import cv2 as cv
import numpy as np

# 2) Aplicar a correção gama para ajustar o brilho de uma imagem monocromática A de entrada 
# e gerar uma imagem monocromática B de saı́da.

img = cv.imread('images/baboon.png', 0)
A = img/255
lam = 1.5
B = A**(1/lam)
dst = np.floor(B*255).astype(np.uint8)

cv.imshow('baboon',dst)
cv.waitKey(0)
cv.destroyAllWindows()