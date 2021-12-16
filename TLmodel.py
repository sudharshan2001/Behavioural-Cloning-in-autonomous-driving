import numpy as np 
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam,SGD, RMSprop, Adadelta
from tensorflow.keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

import matplotlib.pyplot as plt
import pickle5 as pickle
from sklearn.model_selection import train_test_split

pickle_path = './Final Train.pkl'
with open(pickle_path, "rb") as fh:
    data = pickle.load(fh)

imgs = [i for i in data['Image']]
keys = [j for j in data['keys']]

# Splititng the data
X_train, X_test, Y_train, Y_test = train_test_split(imgs, keys, test_size=0.1, random_state=42)

# converting it into float type
X_train = np.asarray(X_train).astype('float32')
X_test = np.asarray(X_test).astype('float32')
Y_train = np.asarray(Y_train).astype('float32')
Y_test = np.asarray(Y_test).astype('float32')

# Normalising
X_train=X_train/255.0
X_test=X_test/255.0

input_shape = (100,100, 1)
densenet = tensorflow.keras.applications.densenet.DenseNet201(include_top=False, weights=None, input_shape=input_shape)

def dense_Model():
    model = Sequential()
    model.add(densenet)
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(5, activation='softmax'))
    optim = SGD(learning_rate=0.001)
    model.compile(loss='categorical_crossentropy', optimizer=optim, metrics=['categorical_accuracy'])
    return model

dense_model = dense_Model()

callbacks = [ReduceLROnPlateau(factor=0.1, patience=20, verbose=1),
             ModelCheckpoint('model bestdense4.h5', verbose=1, save_best_only=True, save_weights_only=False,
                             monitor='val_categorical_accuracy',save_freq='epoch',mode='max')]

history = dense_model.fit(X_train, Y_train, epochs=200, validation_data=(X_test, Y_test), 
                    callbacks=[callbacks], batch_size=64, verbose=1, shuffle=1)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training', 'validation']) 
plt.title('Loss')
plt.xlabel('Epoch')