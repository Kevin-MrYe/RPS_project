import time
import cv2
from PIL import Image, ImageOps
  
# define the countdown func.
def countdown(t,cap):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        cv2.waitKey(125)
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
cap = cv2.VideoCapture(0) ##Open the first camera for video capturing.
ret,frame = cap.read()

# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t),cap)