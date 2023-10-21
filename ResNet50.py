# importação das bibliotecas necessárias
import matplotlib.pyplot as plotter_lib
import numpy as np
import PIL as image_lib
import tensorflow as tflow

from tensorflow.keras.layers import Flatten
from keras.layers.core import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

demo_dataset = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
directory = tflow.keras.utils.get_file(
    'flower_photos', origin=demo_dataset, untar=True)
data_directory = pathlib.Path(directory)

img_height, img_width = 180, 180
batch_size = 32
train_ds = tflow.keras.preprocessing.image_dataset_from_directory(data_directory, validation_split=0.2, subset="training", seed=123,
                                                                  label_mode='categorical', image_size=(img_height, img_width), batch_size=batch_size)

validation_ds = tflow.keras.preprocessing.image_dataset_from_directory(data_directory, validation_split=0.2, subset="validation", seed=123,

                                                                       label_mode='categorical', image_size=(img_height, img_width), batch_size=batch_size)
