import imp
import random
import cv2
from cv2 import imshow
from keras.models import load_model
import numpy as np

#Figure out who win
def play_RPS(index_usr,usr_win_count,cp_win_count):
    cp_poses = ['Rock','Paper','Scissors']
    poses = ['Rock','Paper','Scissors','Nothing']

    # index_usr = input('0.Rock 1.Paper 2.Scissors  3.Nothing')
    usr_pose = poses[index_usr]
    cp_pose = random.choice(cp_poses)
    print('Computer chose ',cp_pose)
    print('User chose ',usr_pose)

    if usr_pose == cp_pose:
        print(f"You both chose {usr_pose}. It's a tie !",)
    elif usr_pose == "Nothing":
        print("Please get ready for your action")
    elif usr_pose == "Rock" and cp_pose == "Scissors":
        usr_win_count = usr_win_count +1
        print("You win !!!")
    elif usr_pose == "Paper" and cp_pose == "Rock":
        usr_win_count = usr_win_count +1
        print("You win !!!")
    elif usr_pose == "Scissors" and cp_pose == "Paper":
        usr_win_count = usr_win_count +1
        print("You win !!!")
    else:
        cp_win_count = cp_win_count + 1
        print("You lose !!!")
    print()
    ## decide who is winner
    if usr_win_count == 3 or cp_win_count == 3:
        if usr_win_count > cp_win_count:    
            print("You are the winner !!!")
        else:
            print("The computer is the winner !!!")
    return usr_win_count,cp_win_count

#Make prediction from the image
def make_predication(frame,data,model):
    #image[y:y+h,x:x+h]
    crop_frame = frame[:,0:480]
    # cv2.imwrite("images/1.jpg",crop_frame)
    resized_frame = cv2.resize(crop_frame, (224, 224), interpolation = cv2.INTER_AREA) ## resampling using pixel area relation.
    image_np = np.array(resized_frame) ## get the image array
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image [0,255] to [0,1]
    data[0] = normalized_image
    prediction = model.predict(data)
    # list_prediction = list(prediction[0])
    #use list.index() to find the maximun

    # if prediction[0][0] > 0.5:
    #     usr_index = 0
    # elif prediction[0][1] > 0.5:
    #     usr_index = 1
    # elif prediction[0][2] > 0.5:
    #     usr_index = 2
    # else:
    #     usr_index = 3
    # print("Rock:",prediction[0][0])
    # print("Paper:",prediction[0][1])
    # print("Scissors:",prediction[0][2])
    # print("Nothing:",prediction[0][3])

    list_prediction = list(prediction[0])
    usr_index = list_prediction.index(max(list_prediction))

    return usr_index

def imshow_with_text(cap,text,text_positon,fontsize,thickness,usr_win_count,cp_win_count):
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text,
                    text_positon,font,
                    fontsize,(0,255,255),
                    thickness,cv2.LINE_AA)
    cv2.putText(frame,"usr:"+str(usr_win_count),
                    (50,20),font,
                    0.8,(0,255,255),
                    2,cv2.LINE_4)
    cv2.putText(frame,"computer:"+str(cp_win_count),
                    (450,20),font,
                    0.8,(0,255,255),
                    2,cv2.LINE_4)
    cv2.imshow('frame', frame)