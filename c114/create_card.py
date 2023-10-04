import cv2

img = cv2.imread('poster.jpg')

rocket = img[120:360, 400:500]
img[0:240, 500:600] = rocket

moon = img[40:110, 100:170]
img[100:170, 50:120] = moon

text_to_show = "Me encanta programar"

cv2.putText(
    img,
    text_to_show,
    (20,200),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(0,0,255)
)


cv2.imshow('Poster', img)

cv2.waitKey(0)

cv2.imwrite('poster_editado.jpeg', img)