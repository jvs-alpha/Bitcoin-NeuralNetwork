import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2

# This is the mnist dataset which is alredy in the tensorflow library
data = keras.datasets.fashion_mnist
(train_images,train_lables),(test_images,test_lables) = data.load_data()
# This is the label for the data
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# Normalization of the data
train_images = train_images/255.0
test_images = test_images/255.0

# 1st LAYER - The Flatten function will make the 2 dimention array of image to 1 dimention to be sent as input so 28*28 = 784 input node
# 2nd LAYER - The Dense Layer is using activation function rectified linear unit
# 3rd LAYER - The Output Dense Layer is using the activation function softmax
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10,activation="softmax")
    ])
# Optimizer is adam
# Loss function used is sparse_categorical_crossentropy
# Metric value used is accuracy
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

# This is for training the data set
model.fit(train_images,train_lables,epochs=5)

# This is for testing the dataset
test_loss, test_acc = model.evaluate(test_images,test_lables)
print("Tested Acc:",test_acc)

prediction = model.predict(test_images) # It takes input as a list

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i],cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_lables[i]])
    plt.title("Prediction " + class_names[np.argmax(prediction[i])])
    plt.show()
