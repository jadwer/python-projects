import cv2

img = cv2.imread("4f.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray,1.1,5)
print(faces)

count = 0
for (x,y,w,h) in faces: 
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    roi_color = img[y:y+h, x:x+w]
    count = count + 1
    name = "face" + str(count) + ".jpg"
    cv2.imwrite(name, roi_color)


cv2.imshow('Rectangulo en la cara', img)
cv2.waitKey(0)