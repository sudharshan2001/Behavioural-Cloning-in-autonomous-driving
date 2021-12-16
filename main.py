from PIL import ImageGrab
import cv2
import numpy as np
import time, os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from getkeys import key_check
from utils import preprocess_to_pred
from tensorflow import keras
from decision_func import left,reverse,right,straight,blank

chosen_model='model bestdense2.h5'

model = keras.models.load_model(chosen_model)

print('Starting..')
time.sleep(1)
array_to_key=['Forward','Reverse','Left','Right','Blank']
last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0,300,800,500))) # Grabbing only the ROI
    screen = preprocess_to_pred(screen) #Preprocession

    predicted_key = model.predict(screen)
    
    time_gap = time.time()-last_time
    last_time = time.time()
    pred_key = np.argmax(predicted_key[0])  # Getting the index of the maximum number in an array
    print(f'{array_to_key[pred_key]}   Time Gap: {time_gap} ') # To check the predicted decision

    # Calling the appropriate function respected to the output
    if pred_key == 0:
        straight(time_gap)
    elif pred_key == 1:
        reverse(time_gap)
    elif pred_key == 2:
        left(time_gap)
    elif pred_key == 3:
        right(time_gap)
    else:
        blank()

    # To break out of loop press Q
    keys = key_check()
    if 'Q' in keys:  
        print('Done')
        break