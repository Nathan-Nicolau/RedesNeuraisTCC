# Criação do modelo da CNN
import tensorflow as tf
import os
import glob
import cv2
import rasterio
from tqdm._tqdm_notebook import tqdm_notebook as tqdm
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.applications import InceptionV3
from keras.src.layers import GlobalAveragePooling2D
from keras.models import Sequential
from keras.layers import Convolution2D, Dropout, Dense, MaxPooling2D
from keras.layers import BatchNormalization
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras import regularizers
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.models import Model
import numpy as np

path = 'C:\\Users\\Gamer\\Documents\\Datasets\\CromossososAjustados_52_x_52\\'
classList = os.listdir(path=path)

x = []  # Vetor que receberá as imagens do Dataset
y = []  # Vetor que receberá as informações das classes

for i in classList:
    pathClass = os.path.join(path, classList[i])
    imgList = os.listdir(pathClass)
    for j in range(len(imgList)):
        pathImg = os.path.join(pathClass, imgList[j])
        src = rasterio.open(pathImg)
        im = src.read()
        # print(str(j) + ' ' + classList[i])
        y.append((i[0:1]))
        x.append(im)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42)
print("Shape of an image in x_train: ", x_train[0].shape)
print("Shape of an image in x_test: ", x_test[0].shape)

le = preprocessing.LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.fit_transform(y_test)
y_train = tf.keras.utils.to_categorical(y_train, num_classes=2)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=2)
y_train = np.array(y_train)
x_train = np.array(x_train)
y_test = np.array(y_test)
x_test = np.array(x_test)

plt.figure(figsize=(10, 10))

img_linhas, img_colunas = 100, 100

rede = InceptionV3(weights='imagenet', include_top=False,
                   input_shape=(img_linhas, img_colunas, 3))

for layer in rede.layers:
    layer.trainable = False

for (i, layer) in enumerate(rede.layers):
    print(str(i) + " " + layer.__class__.__name__, layer.trainable)


def lw(bottom_model, num_classes):
    top_model = bottom_model.output
    top_model = GlobalAveragePooling2D()(top_model)
    top_model = Dense(1024, activation='relu')(top_model)
    top_model = Dense(512, activation='relu',
                      kernel_regularizer=regularizers.l2(0.01))(top_model)
    top_model = Dense(num_classes, activation='softmax')(top_model)
    return top_model


num_classes = 24
FC_head = lw(rede, num_classes)

model = Model(inputs=vgg.input, outputs=FC_head)
print(model.summary())
