import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller

keyboard = Controller()

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)

tipIds = [4, 8, 12, 16, 20]

def drawHandLandmarks (image, hand_landmarks) :
    if hand_landmarks :
        for landmarks in hand_landmarks :
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)

state = None

def countFingers(hand_landmarks, handNo = 0) :
    totalFingers = 0

    if hand_landmarks :
        landmarks = hand_landmarks[handNo].landmark

        fingers = []

        for lm_index in tipIds :
            finger_tip_y = landmarks[lm_index].y
            finger_bottom_y = landmarks[lm_index - 2].y

            if lm_index != 4 :
                if finger_tip_y < finger_bottom_y :
                    fingers.append(1)
                elif finger_tip_y > finger_bottom_y :
                    fingers.append(0)

        totalFingers = fingers.count(1)
    return totalFingers

def magicController (totalFingers, hand_landmarks, handNo = 0) :
    global state

    if totalFingers == 4 and state != "Play":
        print("Play")
        state = "Play"
        keyboard.press(Key.space)

    elif totalFingers == 0 and state != None and state != "Pause":
        print("Pausa")
        state = "Pause"
        keyboard.press(Key.space)

    if hand_landmarks :
        landmarks = hand_landmarks[handNo].landmark

        index_finger = int(landmarks[8].x * 100)
        

        if totalFingers == 1 :
            if index_finger >= 70 and state != "Fordward" :
                print("X: ", index_finger)
                print("Fordward")
                state = "Fordward"
                keyboard.press(Key.right)
            if index_finger >= 30 and index_finger <= 69 :
                state = None
            if index_finger <= 29 and state != "Rewind" :
                print("X: ", index_finger)
                print("Rewind")
                state = "Rewind"
                keyboard.press(Key.left)
    return

while True :
    success, image = cap.read()

    image = cv2.flip(image, 1)

    results = hands.process(image)

    hand_landmarks = results.multi_hand_landmarks

    drawHandLandmarks(image, hand_landmarks)

    num_fingers = countFingers(hand_landmarks)

    magicController(num_fingers, hand_landmarks)

    cv2.putText(image, 'Dedos: %s' % (num_fingers), (650, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)

    cv2.imshow("Control mágico", image)

    if cv2.waitKey(25) == 27 :
        break

cv2.destroyAllWindows()