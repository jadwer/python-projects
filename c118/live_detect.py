import cv2

vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

while (True) : 
    # Captura el video
    # cuadro por cuadro

    ret,frame = vid.read()
    print(cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
#    eyes = eye_cascade.detectMultiScale(gray, 1.5, 5)

    for (x, y, w, h) in faces :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)


    # for (x, y, w, h) in eyes :
    #     cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Web cam", frame)

    if cv2.waitKey(25) == 32 :
        break

vid.release()

cv2.destroyAllWindows()