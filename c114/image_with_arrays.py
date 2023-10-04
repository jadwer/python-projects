import numpy as np
import cv2

black = np.zeros([600, 600])
# print(black)
# black[1][1] = 1
# print(black)

f_row = black[1:2]
print("row: " + str(f_row))

f_col = black[:,1:2]
print("col: " + str(f_col))

black[200:400,200:400] = 255
#f_mat = black[2:4,2:4]
# print(f_mat)
print(black)

cv2.imshow('En negro', black)
cv2.waitKey(0)