import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from utils import segment

df=pd.read_csv('trainingdatareg.csv')
df.info()

w, s, a, d, bl = ([] for i in range(5))

# appending the respective key to it's column, the index is based on the index of it in string format 
for i in range(0,len(df)):
    w.append(int(df.loc[i]['Key Pressed'][1]))
    s.append(int(df.loc[i]['Key Pressed'][4]))
    a.append(int(df.loc[i]['Key Pressed'][7]))
    d.append(int(df.loc[i]['Key Pressed'][10]))
    bl.append(int(df.loc[i]['Key Pressed'][13]))


df['w'],df['s'],df['a'],df['d'],df['bl'] = w, s, a, d, bl

df1=df.drop(['Unnamed: 0', 'Key Pressed'],axis=1)

# To check proportions of data
def check_proportions(df1):
    print('w', df1[df1['w']==1].value_counts().sum())
    print('s',df1[df1['s']==1].value_counts().sum())
    print('a',df1[df1['a']==1].value_counts().sum())
    print('d',df1[df1['d']==1].value_counts().sum())
    print('bl',df1[df1['bl']==1].value_counts().sum())

# check_proportions(df1=df1)

# check for tha n value according to your data proportions
index_w = df1.query('w == 1').sample(n=6100).index
index_bl = df1.query('bl == 1').sample(n=4913).index

df2=df1.drop(index_w)
df2=df2.drop(index_bl)
df2.reset_index(drop=True, inplace=True)

# Load data from CSV
def load_data_fromcsv(data):
    path = []
    key = []
    images = []
    for i in range(len(data)):
        temp_path = data.iloc[i][1]
        temp_key = data.iloc[i][2:].values
        image = segment(temp_path)
        images.append(image)
        path.append(temp_path)
        key.append(temp_key)
        
        
    path = np.asarray(path)
    key = np.asarray(key)
    return images, key

images, keys = load_data_fromcsv(df2)

# Loadinf it to a series 
final_data = pd.DataFrame({'Image':pd.Series([i for i in images], index=[k for k in range(len(images))]),
                           'keys': pd.Series([j for j in keys], index=[l for l in range(len(keys))])})

# Saving it as a pickle file
final_data.to_pickle('./Final Train.pkl')