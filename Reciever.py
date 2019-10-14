import socket
import os
os.environ['OPENCV_IO_MAX_IMAGE_PIXELS']=str(2**64)
import cv2
import numpy as np
import time
import warnings
from time import sleep
warnings.simplefilter("ignore", DeprecationWarning)

HOST = 'localhost'
PORT = 50505

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()


cv2.namedWindow("Live Webcam")
vc = cv2.VideoCapture(0)

while True:
    frame = conn.recv(8192)
    rval, frame = vc.read()
    cv2.imshow("Live Webcam", frame)
    print(frame)
    #time.sleep(2)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Live Webcam")