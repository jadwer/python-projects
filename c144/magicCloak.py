import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('magic.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(2)
gb = 0

for i in range(10):
    ret, bg = cap.read()

bg = np.flip(bg, axis = 1)

cv2.imshow("Fondo", bg)
    
while (cap.isOpened()) :
    ret, img = cap.read()

    if not ret :
        break
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 150, 110])
    upper_red = np.array([340, 185, 185])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    lower_green = np.array([170, 120, 70])
    upper_green = np.array([180, 255, 255])
    mask_green = cv2.inRange(hsv, lower_red, upper_red)

    cv2.imshow("Capa Invisible", mask_red)

    mask_1 = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask_1 = cv2.morphologyEx(mask_red, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    mask_2 = cv2.bitwise_not(mask_1)

    res_1 = cv2.bitwise_and(img, img, mask=mask_2)

    res_2 = cv2.bitwise_and(bg, bg, mask=mask_1)

    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
    
    output_file.write(final_output)

    cv2.imshow("Magic", final_output)




    if cv2.waitKey(1) == 27 :
        break

cap.release()
output_file.release()
cv2.destroyAllWindows()