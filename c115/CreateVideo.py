import cv2
import os

path="Images"

images = []

for file in os.listdir(path) :
    name, ext = os.path.splitext(file)

    if ext in ['.jpg'] :
        file_name = path + "/" + file

        print(file_name)

        images.append(file_name)
    
#images.sort(reverse=True)
images.sort()
count = len(images)
print(count)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('dawn.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 6, size)

for image in range(count-1, 0, -1) :
    frame = cv2.imread(images[image])
    out.write(frame)

out.release()
print("listo")