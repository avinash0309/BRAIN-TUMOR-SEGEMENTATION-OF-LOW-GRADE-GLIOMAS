# -*- coding: utf-8 -*-
"""UnetBatchnorm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rIs-S0pJRUO10n860TTwhk84AHVJXqwJ

# U-NET ARCHITECTURE
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
import cv2
from keras import layers
from keras.models import Sequential
from keras.models import Input
from keras.models import Model
from keras.layers.convolutional import Conv2D
from keras.layers import Conv2DTranspose
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Activation
from keras.layers import ReLU
from keras.layers import LeakyReLU
from keras.layers import Dropout
from keras.layers import BatchNormalization
from keras.layers import Dropout
from keras.layers import UpSampling2D
from keras.layers import MaxPooling2D
from keras.layers import Concatenate
from keras.layers import Reshape
from keras.losses import binary_crossentropy
from keras.layers import add
from keras.utils import plot_model
from keras.optimizers import Adam

imagesize = 256
batch_size = 32

def Downsample_Block(input_data,Number_of_filters):
  D = Conv2D(Number_of_filters,kernel_size=(3,3),activation='relu',padding='same',strides=1)(input_data)
  D = BatchNormalization()(D)
  D = Conv2D(Number_of_filters,kernel_size=(3,3),activation='relu',padding='same',strides=1)(D)
  D = BatchNormalization()(D)
  P = MaxPooling2D(2)(D)
  return D,P

def Bridge_Block(input_data,Number_of_filters):
  D = Conv2D(Number_of_filters,kernel_size=(3,3),activation='relu',padding='same',strides=1)(input_data)
  D = BatchNormalization()(D)
  D = Conv2D(Number_of_filters,kernel_size=(3,3),activation='relu',padding='same',strides=1)(input_data)
  D = BatchNormalization()(D)
  return D

def Upsample_Block(input_data,skip_connection,Number_of_filters):
  U = UpSampling2D(size=(2,2))(input_data)
  skip_Connect = Concatenate()([U,skip_connection])
  D = Conv2D(Number_of_filters,kernel_size=(3,3),activation='relu',padding='same',strides=1)(skip_Connect)
  D = BatchNormalization()(D)
  D = Conv2D(Number_of_filters,kernel_size=(3,3),activation='relu',padding='same',strides=1)(D)
  D = BatchNormalization()(D)
  return D

def UNET_model_batchnorm():
  filters = [32,64,128,256,512]
  inputs = Input((imagesize,imagesize,1))

  A1,P1 = Downsample_Block(inputs,filters[0])
  A2,P2 = Downsample_Block(P1,filters[1])
  A3,P3 = Downsample_Block(P2,filters[2])
  A4,P4 = Downsample_Block(P3,filters[3])

  bridge_output = Bridge_Block(P4,filters[4])

  U1 = Upsample_Block(bridge_output,A4,filters[3])
  U2 = Upsample_Block(U1,A3,filters[2])
  U3 = Upsample_Block(U2,A2,filters[1])
  U4 = Upsample_Block(U3,A1,filters[0])

  output = Conv2D(1,kernel_size=(1,1),activation='sigmoid')(U4)
  model = Model(inputs,output)

  return model

Unet = UNET_model_batchnorm()
plot_model(Unet)






