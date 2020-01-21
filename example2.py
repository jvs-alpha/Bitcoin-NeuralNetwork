import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load the data
data = keras.datasets.imdb

# Sectioned the data for trainging set and test set and num_words mean top 10000 words
(train_data,train_lables),(test_data,test_lables) = data.load_data(num_words=10000)

#index of the data
word_index = data.get_word_index()

word_index = {k:(v+3) for k,v in word_index.items()} # This will increase the value of the word:value by three
# To add these
# New values
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["UNK"] = 2
word_index["UNUSED"] = 3

# This is a reverse loop for reverse the values in the key:value to value:key
reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])
train_data = keras.preprocessing sequence.pad_sequences(train_data,value=word_index["<PAD>"],padding="post",maxlen=250)
test_data = keras.preprocessing sequence.pad_sequences(test_data,value=word_index["<PAD>"],padding="post",maxlen=250)

# This function is for converting the values into the string values
def decode_review(text):
    return "".join([reverse_word_index.get(i,"?") for i in text])

# Building the Model
model = keras.Sequential()
model.add(keras.layers.Embedding(10000,16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16,activation="relu"))
model.add(keras.layers.Dense(1,activation="sigmoid"))
