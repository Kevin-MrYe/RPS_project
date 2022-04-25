import cv2
from keras.models import load_model
import numpy as np
from game_logic import imshow_with_text, play_RPS,make_predication
import time


model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0) ##Open the first camera for video capturing.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) 
## 4D array, image size and RGB values
 
TIMER = 5  #countdown
cp_win_count = 0  # victories of computer
usr_win_count = 0 # victories of user

while True: 

    if cp_win_count == 0 and usr_win_count == 0:
 
        imshow_with_text(cap,"Press S to start",(150,250),1.5,2,usr_win_count,cp_win_count)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        prev = time.time() 
        while TIMER > 0:

            imshow_with_text(cap,str(TIMER),(200,250),7,4,usr_win_count,cp_win_count)
            cv2.waitKey(125)

            ##countdown
            cur = time.time()
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER -1
        else:
            ret,frame = cap.read()
            cv2.imshow('frame',frame)
            # cv2.imwrite('images/frame_'+str(cur)+".jpg",frame)
            cv2.waitKey(500)
            usr_index = make_predication(frame,data,model)
            usr_win_count,cp_win_count = play_RPS(usr_index,usr_win_count,cp_win_count)

    #Press c to continue
    if usr_win_count == 3 or cp_win_count == 3:

        imshow_with_text(cap,"Press C to continue !",(120,250),1.5,2,usr_win_count,cp_win_count)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            usr_win_count = 0
            cp_win_count = 0

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    TIMER = 5

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

