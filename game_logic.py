import imp
import random
import cv2
from keras.models import load_model
import numpy as np
import time

def play_RPS(index_usr,usr_win_count,cp_win_count):
    
    cp_poses = ['Rock','Paper','Scissors']
    poses = ['Rock','Paper','Scissors','Nothing']

    cp_pose = random.choice(cp_poses)
    
    # index_usr = input('0.Rock 1.Paper 2.Scissors  3.Nothing')
    usr_pose = poses[index_usr]

    print('Computer chose ',cp_pose)
    print('User chose ',usr_pose)

    if cp_pose == usr_pose:
        print(f"You both chose {usr_pose}. It's a tie !",)
    elif usr_pose == "Rock":
        if cp_pose == "Paper":
            cp_win_count = cp_win_count +1
            print("You lose ...")
        else:
            usr_win_count = usr_win_count +1
            print("You win !!!")
    elif usr_pose == "Paper":
        if cp_pose == "Scissors":
            cp_win_count  = cp_win_count  +1
            print("You lose ...")
        else:
            usr_win_count = usr_win_count +1
            print("You win !!!")
    elif usr_pose == "Scissors":
        if cp_pose == "Rock":
            cp_win_count = cp_win_count +1
            print("You lose ...")
        else:
            usr_win_count = usr_win_count +1
            print("You win !!!")
    else:
        print("Please get ready for your action")
    print()
    return usr_win_count,cp_win_count

def make_predication(frame,data,model):
    height, width, channels = frame.shape
    crop_frame = frame[:,0:480]
    resized_frame = cv2.resize(crop_frame, (224, 224), interpolation = cv2.INTER_AREA) ## resampling using pixel area relation.
    image_np = np.array(resized_frame) ## get the image array
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image [0,255] to [0,1]
    data[0] = normalized_image
    prediction = model.predict(data)
    if prediction[0][0] > 0.5:
        usr_index = 0
    elif prediction[0][1] > 0.5:
        usr_index = 1
    elif prediction[0][2] > 0.5:
        usr_index = 2
    else:
        usr_index = 3
    return usr_index
