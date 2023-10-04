import cv2
import numpy as np

img = cv2.imread('butterfly.jpg')

cv2.imshow('Mi imagen', img)

# print(img)

gray_img = cv2.cvtColor(img, 69)

cv2.imshow("Escala de grises: %", gray_img)

cv2.waitKey(0)

