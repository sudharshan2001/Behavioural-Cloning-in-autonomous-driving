import cv2
import numpy as np


def segment(image):
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    segment = gray[300:500,:]
    resized_image = cv2.resize(segment, (100, 100))
    return resized_image

def keys_to_OHE(keys):
    if 'W' in keys:
        output = [1,0,0,0,0]
    elif 'S' in keys:
        output = [0,1,0,0,0]
    elif 'A' in keys:
        output = [0,0,1,0,0]
    elif 'D' in keys:
        output = [0,0,0,1,0]
    else:
        output = [0,0,0,0,1]
    return output

def preprocess_to_pred(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    # image = cv2.GaussianBlur(gray, (5,5), 0 )
    resized_image = cv2.resize(image, (100, 100)) # Resizing the image to 100X100 
    resized_image = np.array(resized_image.reshape((1,100,100,1))) # Reshaping it to the model input format
    resized_image = resized_image/255.0 
    return resized_image