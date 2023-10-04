import cv2


''' # Para capturar webcam
vid = cv2.VideoCapture(1)

if(vid.isOpened() == False):
    print("Error: no se puede leer la cámara")
else : 
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(height)
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(width)
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    print(fps)
    
    while (True) :
        ret, frame = vid.read()

        cv2.imshow("Camara web", frame)

        if cv2.waitKey(1) == 32:
            break
    vid.release()
'''

vid = cv2.VideoCapture('AnthonyShkraba.mp4')

if(vid.isOpened() ==False) : 
    print('Error: No se puede abrir el video')
else : 
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    print(fps) #50 fps
    out = cv2.VideoWriter(
        'Boxing.mp4',
        cv2.VideoWriter_fourcc(*'mp4v'),
        25, # en lugar de fps
        (width, height)
        )
    while(True) : 
        ret, frame = vid.read()
        cv2.imshow("Video", frame)

        out.write(frame)

        if(cv2.waitKey(1) == 32) : 
            break
    
    vid.release()
    out.release()
    cv2.destroyAllWindows()

