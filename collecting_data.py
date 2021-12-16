from PIL import ImageGrab
import cv2
import numpy as np
import pandas as pd
import time, os
from getkeys import key_check
from utils import keys_to_OHE

last_time = time.time()
df = pd.DataFrame(None,columns=['Image Name','Image Path','Key Pressed'])  #creating a dummy dataframe


print('Starting..')
time.sleep(1)
paused = False
while True:
    if not paused:
        screen = np.array(ImageGrab.grab(bbox=(0,0,800,640))) # Grabbing the picture of game windows

        last_time = time.time()
        image_path = f".\\Training_Data\\trainingdata\\{last_time}.jpg"  #Make sure to create the folder
        # cv2.imshow('Python Window', screethe picture
        cv2.imwrite(image_path,screen) #Saving it
        keys = key_check()  # Scans for the keys
        output = keys_to_OHE(keys) 
        
        df = df.append({"Image Name":str(last_time)+'.jpg', "Image Path":image_path,"Key Pressed":output} # Append the required field to dataframe
        ,ignore_index = True)

    keys = key_check()
    if 'T' in keys:
        if paused:
            paused = False
            print('Unpaused!')
            time.sleep(1)
        else:
            print('Pausing!')
            paused = True
            time.sleep(1)
    elif 'Q' in keys:  
        break

print(df.head())
df.to_csv('trainingdatareg.csv')  # Saving the dataframe
