import cv2
import mediapipe as mp

wCam, hCam = 720, 640
cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)

def drawHandLandmarks (image, hand_landmarks):
    if hand_landmarks :
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)

tipIds = [4, 8, 12, 16, 20] 

def fingerPosition(image, handNo = 0) :
    lmList = []
    if results.multi_hand_landmarks :
        myHand = results.multi_hand_landmarks[handNo]

        for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
    return lmList


while True:
    success, image = cap.read()
    
    image = cv2.flip(image, 1)

    results = hands.process(image)

    hand_landmarks = results.multi_hand_landmarks

    drawHandLandmarks(image, hand_landmarks)

    points = fingerPosition(image)
    #[id_dedo, x, y]

    if len(points) != 0 :
        fingers = []

        # Recorrer del 0 al 5 para obtener los puntos de las yemas
        # tipIds = [0:4, 1:8, 2:12, 3:16, 4:20]
        for id in range(0, 5) :
            # Si no es el pulgar (id == 0 es el punto 4 que corresponde al pulgar)
            if id != 0 :
                # Si el punto Y es menor a esa posición -2, decimos que está levantado
                if points[tipIds[id]][2] < points[tipIds[id]-2][2] : 
                    # Si el punto dado para el dedo 1 es menor al punto dado Y-2, agregalo
                    fingers.append(1)
                # Si el punto Y es mayor a esa posición -2, decimos que está recogido
                if points[tipIds[id]][2] > points[tipIds[id]-2][2] : 
                    fingers.append(0)
            # Si es el pulgar, lo mismo de arroba pero se toma la X
            else :
                if points[tipIds[id]][1] > points[tipIds[id]-2][1] : 
                    fingers.append(1)
                if points[tipIds[id]][1] < points[tipIds[id]-2][1] : 
                    fingers.append(0)
        
        totalFingers = fingers.count(1)

        cv2.putText(image, 'Dedos: %s' % (totalFingers), (650, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

        print(totalFingers)

    cv2.imshow("Ventana de captura", image)

    if cv2.waitKey(1) == 32 : 
        break
    
cv2.destroyAllWindows()