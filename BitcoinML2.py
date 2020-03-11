import pandas as pd
from keys import *
from binance.client import Client
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM,Dense


# This area is for reading the data and reshapeing as we need it
BTC = pd.read_csv("data.csv",index_col=0)
BTC["close"] = BTC["close"].astype("float")
data = BTC.iloc[:,4].astype("float").values
data = np.reshape(data,(len(data),1))  # we need two dimension array for the MinMaxScaler to work

# This will normalize the data with the sigmoid method
scaler = MinMaxScaler()
data = scaler.fit_transform(data)   # This will fit the data to the need transform it

# This will segment the data to training set and test set
training_set = data[:2268]
test_set = data[2268:]

# Shift the values of the data by one step to train the values with the reference
x_train = training_set[0:len(training_set)-1]
y_train = training_set[1:len(training_set)]

# Shift of the data to check with trained model
x_test = test_set[0:len(test_set)-1]
y_test = test_set[1:len(test_set)]

# reshape the data to 3-d
x_train = np.reshape(x_train,(len(x_train),1,x_train.shape[1]))
x_test = np.reshape(x_test,(len(x_test),1,x_test.shape[1]))


# Creting the model
model = Sequential()
model.add(LSTM(256,return_sequences=True,input_shape=(x_train.shape[1],x_train.shape[2])))
model.add(LSTM(256))
model.add(Dense(1))
model.compile(loss="mean_squared_error",optimizer="adam")

# Training the model and prediction
model.fit(x_train,y_train,epochs=100,batch_size=16,shuffle=False)
predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(predicted_price)
real_price = scaler.inverse_transform(y_test)

# Save the model
model.save("BTCPP.h5")

# To display the predicted value
plt.figure(figsize=(20,8))
plt.plot(predicted_price,color="red",label="Predicted price")
plt.plot(real_price,color="blue",label="Real Price")
plt.title("Prediction vs Real from 2019-10-10 09:30:00 to 2020-02-15 17:30:00")
plt.xlabel("time")
plt.ylabel("price")
plt.show()
