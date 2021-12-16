# Behavioural-Cloning-in-autonomous-driving

Using CNN to mimic the driver based on training data from Torcs.

## Approach 
  First, the data was collected from the game while i played using collecting_data.py script. Images of the game window and the keys i pressed are simultaneously recorded and stored in a dataframe('trainingdatareg.csv') in the path declared there.
  Then the data is cleaned by balancing it's proportion, removed unwanted columns and then cropped out the ROI for feeding it into the model using datacleaning.py script
  Trained various model using transfer learning like DenseNet, VGG19, EfficientNet etc and chose the model with high accuracy ('DenseNet') with the help of kaggle GPU and saved it.
  Then tested the model.
  
## Result
  As of now the model detects lane and adjust it's input to it and performs well in a straight lane but it gets cranky while turning. Need to adjust it later.

![selfdrive](https://user-images.githubusercontent.com/72936645/146306891-0323ee95-d889-4a07-a60c-04fb2f9405e3.gif)

# Reference:
  Sentdex:https://www.youtube.com/c/sentdex
  
  https://arxiv.org/abs/1910.06734
  
  https://towardsdatascience.com/behavioural-cloning-applied-to-self-driving-car-on-a-simulated-track-5365e1082230
  
