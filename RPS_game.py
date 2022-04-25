import cv2
from keras.models import load_model
import numpy as np
from game_logic import play_RPS,make_predication,countdown
import time

TIMER = int(5)
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0) ##Open the first camera for video capturing.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) ## 4D array, image size and RGB values

cp_win_count = 0 
usr_win_count = 0

while True: 

    if cp_win_count == 0 and usr_win_count == 0:
        ret, frame = cap.read() ##ret indicates if the read was successful, frmae is image itself
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"Press S to start !",
                            (150,250),font,
                            1.5,(0,255,255),
                            2,cv2.LINE_AA)
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        prev = time.time() #
        while TIMER > 0:
            ret, frame = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,str(TIMER),
                        (200,250),font,
                        7,(0,255,255),
                        4,cv2.LINE_AA)
            cv2.imshow('frame',frame)
            cv2.waitKey(125)

            cur = time.time()
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER -1
        else:
            ret,frame = cap.read()
            cv2.imshow('frame',frame)
            cv2.waitKey(1000)
            usr_index = make_predication(frame,data,model)
            usr_win_count,cp_win_count = play_RPS(usr_index,usr_win_count,cp_win_count)

    if usr_win_count == 3 or cp_win_count == 3:
        if usr_win_count > cp_win_count:    
            print("You defeated the computer !!!")
        else:
            print("The computer defeated you !!!")

   
        ret, frame = cap.read()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"Press C to continue !",
                        (150,250),font,
                        1.5,(0,255,255),
                        2,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            usr_win_count = 0
            cp_win_count = 0
        elif cv2.waitKey(1) & 0xFF == ord('q'): # Press q to close the window
            break

    TIMER = int(5)



# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()