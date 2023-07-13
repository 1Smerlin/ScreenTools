import cv2
import numpy as np
import pyautogui
import time

# Video Programm
screen = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"MP4V")
output = cv2.VideoWriter("output.mp4", fourcc, 30, screen)

start_time = time.time()
frame_count = 0

while True:
    if time.time() - start_time >= 5:  # Stoppt nach 5 Sekunden
        break
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    frame_count += 1

output.release()

print("Aufnahmezeit: {} Sekunden".format(frame_count/30))
