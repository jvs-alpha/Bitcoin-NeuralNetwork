import pandas as pd
from keys import *
from binance.client import Client
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dense



BTC = pd.read_csv("data.csv",index_col=0)
BTC["close"] = BTC["close"].astype("float")
data = BTC.iloc[:,[4]].astype("float").values
scaler = MinMaxScaler()
data = scaler.fit_transform(data)

training_set = data[:2268]
test_set = data[2268:]

x_train = training_set[0:len(training_set)-1]
y_train = training_set[1:len(training_set)]

x_test = test_set[0:len(test_set)-1]
y_test = test_set[1:len(test_set)]

print(x_train.shape)
