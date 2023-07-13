import cv2
import numpy as np
import pyautogui

# Video Programm
screen = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = 30
record_seconds = 5
frame_count = int(fps * record_seconds)

output = cv2.VideoWriter("output.mp4", fourcc, fps, screen)

for i in range(frame_count):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)

output.release()
