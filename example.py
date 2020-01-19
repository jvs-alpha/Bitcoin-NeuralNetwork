import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2

# This is the mnist dataset which is alredy in the tensorflow library
data = keras.datasets.fashion_mnist
(train_images,train_lables),(test_images,test_lables) = data.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images/255.0
test_images = test_images/255.0
plt.imshow(train_images[7],cmap=plt.cm.binary)
plt.show()