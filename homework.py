import cv2
import time
import random


class homework:
    start_time = time.time()


    def capture():

        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while (result):
            ret, frame = videoCaptureObject.read()
            cv2.imwrite("C:\Parth\Visual Studio - Whithat Junior\Python\Project - 102\homework.png", frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    capture()
