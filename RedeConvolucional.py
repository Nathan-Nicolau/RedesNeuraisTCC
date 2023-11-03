# from google.colab import drive
# import os
# drive.mount('/content/drive')
# Até aqui deu certo

import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from matplotlib import rcParams
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
# Importação das classes/bibliotecas para desenvolvimento da Rede Convolucional
from keras.models import Model, Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout, Activation
import tensorflow as tf
# from tensorflow.keras.optimizer import Adam
from keras.optimizers import Adam
from keras.activations import relu
from keras.losses import binary_crossentropy
from keras import backend as K
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
# from keras.utils import np
from keras import utils as utils
import seaborn as sns

path = 'C:\\Users\\Gamer\\Documents\\Datasets\\CromossososAjustados_52_x_52\\'
classList = os.listdir(path=path)

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
plt.style.use('fivethirtyeight')
rcParams['figure.figsize'] = 18, 6
x = []  # Vetor que receberá as imagens do Dataset
y = []  # Vetor que receberá as informações das classes
i = 0

for i in range(len(classList)):
    pathClass = os.path.join(path, classList[i])
    imgList = os.listdir(pathClass)
    for j in range(len(imgList)):
        pathImg = os.path.join(pathClass, imgList[j])
        src = rasterio.open(pathImg)
        im = src.read()
        im = im.transpose([1, 2, 0])
        im1 = im[:, :, 1:9]
        im2 = im[:, :, 11:]
        im = np.dstack((im1, im2))
        # print(str(j) + ' ' + classList[i])
        y.append(i)
        x.append(im)
    i += 1


x = np.array(x)
y = np.array(y)


classe, qtd = np.unique(y, return_counts=True)
df = pd.DataFrame(data=qtd, index=classList, columns=['Amostras'])
ax = sns.barplot(x=df.index, y="Amostras", data=df)

y = utils.to_categorical(y)

xTrain, xTest, yTrain, yTest = train_test_split(
    x, y, test_size=0.3, random_state=10)

# print('Dados x de Treinamento: ' + str(xTrain.shape))
# print('Dados x de Testes' + str(yTest.shape))
#
# print('Dados y de Treinamento: ' + str(yTrain.shape))
# print('Dados y de Testes: ' + str(yTest.shape))

xTest = xTest/10000.0
xTrain = xTrain/10000.0
xTrain.shape[1:]
print(str(xTrain.shape[1:]))

Rede = Sequential()
Rede.add(Conv2D(32, (3, 3), kernel_initializer="he_normal",
         padding="same", input_shape=(xTrain.shape[1:])))
Rede.add(Activation('relu'))
Rede.add(MaxPooling2D(pool_size=(2, 2), strides=2))
Rede.add(Conv2D(64, (3, 3), kernel_initializer='he_normal', padding='same'))
Rede.add(Activation('relu'))
Rede.add(MaxPooling2D(pool_size=(2, 2), strides=2))
Rede.add(Conv2D(128, (3, 3), kernel_initializer='he_normal', padding='same'))
Rede.add(Activation('relu'))
Rede.add(MaxPooling2D(pool_size=(2, 2), strides=2))
Rede.add(Conv2D(256, (3, 3), kernel_initializer='he_normal', padding='same'))
Rede.add(Activation('relu'))
Rede.add(MaxPooling2D(pool_size=(2, 2), strides=2))
Rede.add(Flatten())
Rede.add(Dropout(0.5))
Rede.add(Dense(512))
Rede.add(Activation('relu'))
Rede.add(Dense(24))
Rede.add(Activation('softmax'))
Rede.compile(loss='categorical_crossentropy',
             optimizer=Adam(lr=0.00001), metrics=['accuracy'])
Rede.summary()
# Parâmetros podem ser mudados
history = Rede.fit(x=xTrain, y=yTrain, batch_size=5, epochs=5,
                   verbose=1, shuffle=True, validation_split=0.2)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Resultados de precisão da RNC')
plt.ylabel('Precisão')
plt.xlabel('Épocas')
plt.legend(['Dados de treinamento', 'Dados de validação'], loc='lower right')
plt.show()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Resultados de perda da RNC')
plt.ylabel('Perda')
plt.xlabel('Épocas]')
plt.legend(['Daoos de treinamento', 'Dados de testes'], loc='upper right')
plt.show()
predict = Rede.predict(xTest)
pred = np.argmax(predict, axis=1)
true = np.argmax(yTest, axis=1)
accuracy = accuracy_score(true, pred)
# print('Precisão Global:(porcentagem)' + accuracy * 100 + "%")
# print(classification_report(true,pred))
