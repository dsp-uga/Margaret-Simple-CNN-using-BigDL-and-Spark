#from __future__ import print_function
import keras
from keras.callbacks import EarlyStopping
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, MaxPooling2D,merge,MaxPooling3D,Conv3D,concatenate
from keras.layers import Activation, Dropout, Flatten, Dense,Merge,Input, Dense,Reshape,BatchNormalization
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras import backend as K
from keras.models import Model
#from deform_conv.layers import ConvOffset2D

from keras import regularizers 
from keras import backend as K
#from keras.optimizers import Adam
#from keras.callbacks import ModelCheckpoint
import pprint
import random
import numpy as np
import os
import shutil
import cv2
import math
#import image
from keras.layers.normalization import BatchNormalization as bn
from scipy.misc import imsave
import numpy as np
import time
#from theano.tensor import _shared
from sklearn import metrics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
import itertools as it
import glob
#import customgen as cg

from sklearn.utils import class_weight
X1_totaldata=[]
X2_totaldata=[]
CUDA_VISIBLE_DEVICES = [1]
os.environ['CUDA_VISIBLE_DEVICES']=','.join([str(x) for x in CUDA_VISIBLE_DEVICES])
#malign =46   /3 15 15 15 
#benign =47    /3   15  15   16  
from keras import backend as K
def weighted_categorical_crossentropy(weights):
    """
    A weighted version of keras.objectives.categorical_crossentropy
    
    Variables:
        weights: numpy array of shape (C,) where C is the number of classes
    
    Usage:
        weights = np.array([0.5,2,10]) # Class one at 0.5, class 2 twice the normal weights, class 3 10x.
        loss = weighted_categorical_crossentropy(weights)
        model.compile(loss=loss,optimizer='adam')
    """
    
    weights = K.variable(weights)
        
    def loss(y_true, y_pred):
        # scale predictions so that the class probas of each sample sum to 1
        y_pred /= K.sum(y_pred, axis=-1, keepdims=True)
        # clip to prevent NaN's and Inf's
        y_pred = K.clip(y_pred, K.epsilon(), 1 - K.epsilon())
        # calc
        loss = y_true * K.log(y_pred) * weights
        loss = -K.sum(loss, -1)
        return loss
    
    return loss




for control in range(1,2):
    

    X_train=np.load("X_train1.npy")
    y_train=np.load("y_train1.npy")

    zipped_stuff=zip(X_train,y_train)
    random.shuffle(zipped_stuff)
    X_train,y_train=zip(*zipped_stuff)
    X_train=np.array(X_train)
    y_train=np.array(y_train)
    y_train = keras.utils.to_categorical(y_train, 9)

    #X_test=X_train[6000:]
    #X_train=X_train[0:6000]

    
    #y_test=y_train[6000:]
    #y_train=y_train[0:6000]
    
    l2_lambda = 0.0002
    DropP = 0.3
    kernel_size=3
    
    inputthree=Input(shape=(32,32,1), dtype='float32',name='inputthree')      
    

    
    

    conv1a = Conv2D( 64, (kernel_size, kernel_size), activation='relu', padding='same', 
                    )(inputthree)

    
    
    
    #conv1a = bn()(conv1a)

    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1a)
    
    conv1b = Conv2D(64, (kernel_size, kernel_size), activation='relu', padding='same',
                    )(pool1)

    #conv1b = bn()(conv1b)

    pool2 = MaxPooling2D(pool_size=(2, 2))(conv1b)



    conv1c = Conv2D(128, (kernel_size, kernel_size), activation='relu', padding='same',
                    )(pool2)

    #conv1c = bn()(conv1c)
    
    pool3= MaxPooling2D(pool_size=(2, 2))(conv1c)
    

    conv1d = Conv2D(256, (kernel_size, kernel_size), activation='relu', padding='same',
                    )(pool3)

    #conv1d = bn()(conv1d)

    pool4= MaxPooling2D(pool_size=(2, 2))(conv1d)   




    conv1g = Conv2D(512, (1, 1), activation='relu', padding='same',
                    )(pool4)

    #conv1g = bn()(conv1g)

    flatten1=Flatten()(conv1g)
    


    
    
    #layerfinal4=Flatten()(downsample3)
    output=Dense(9,activation='softmax',name='output')(flatten1)
    #from keras.optimizers import Adam
   
    finalmodel = Model(inputs=[inputthree], outputs=[output])#outputs=[output1,output2,output4,output5,output])
    finalmodel.compile(optimizer='adadelta',loss=weighted_categorical_crossentropy([1.9,1.19,1,6.196,71.16,3.91,7.4,2.395,2.90]),metrics=['accuracy'])
    finalmodel.summary()

    


    
    xyz=keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, verbose=1, mode='auto')
    
    finalmodel.fit([X_train], [y_train],#,y_train,y_train,y_train,y_train],
                    batch_size=8,
                    epochs=100,
                    validation_split=0.04,
                    #validation_data=([X2_validate,X3_validate],[y_validate,y_validate,y_validate,y_validate,y_validate]),
                    shuffle=True,
                    callbacks=[xyz],
                   )
import h5py
finalmodel.save('simple_nw.h5')
X_test=np.load("X_test1.npy")
predicted=finalmodel.predict(X_test,  batch_size=8)
towrite=[]
towrite1=[]
final_predicted=predicted
prior=[1155.0/8147.0,1858.0/8147.0,2206.0/8147.0,356.0/8147.0,31.0/8147.0,563.0/8147.0,298.0/8147.0,921.0/8147.0,759.0/8147.0]
for i in range(0,len(final_predicted)):

  
  
  towrite.append(np.argmax(final_predicted[i])+1)
  
  for k in range(0,9):
    final_predicted[i,k]=final_predicted[i,k]*prior[k]
  towrite1.append(np.argmax(final_predicted[i])+1)

    
  
np.savetxt('predicted_tosubmit.txt',towrite,delimiter=',')
np.savetxt('predicted_tosubmit_prior.txt',towrite1,delimiter=',')


   
