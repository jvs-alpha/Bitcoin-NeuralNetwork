from keys import *
import datetime
from binance.client import Client
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
client = Client(APIKey,SecretKey)
symbol = "BTCUSDT"
BTC = client.get_historical_klines(symbol=symbol,interval=Client.KLINE_INTERVAL_30MINUTE,start_str="1 year ago UTC")
BTC = pd.DataFrame(BTC,columns=["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume","Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"])
BTC["Open time"] = pd.to_datetime(BTC["Open time"],unit="ms")
BTC.set_index("Open time",inplace=True)
BTC["Close"] = BTC["Close"].astype("float")
# BTC["Close"].plot(figsize=(20,10),title="1 year")
# plt.show()
data = BTC.iloc[:,3:4].astype("float").values
scaler = MinMaxScaler()
data = scaler.fit_transform(data)
training_set = data[:10000]
test_set = data[10000:11000]

x_train = training_set[0:len(training_set)-1]   # The value that is used in prediction
y_train = training_set[1:len(training_set)]     # The reference value that is used
# We can see that the y_train is shifted one value from the start to the end
# which means the NN will reain use the x_train as the input and the y_train as the ideal output

x_test = test_set[0:len(test_set)-1]
y_test = test_set[1:len(test_set)]

x_train = np.reshape(x_train,(len(x_train),1,x_train.shape[1]))
x_test = np.reshape(x_test,(len(x_test),1,x_test.shape[1]))

model = Sequential()
model.add(LSTM(256,return_sequences=True,input_shape=(x_train.shape[1],x_train.shape[2])))
model.add(LSTM(256))
model.add(Dense(1))

model.compile(loss="mean_squared_error",optimizer="adam")
model.fit(x_train,y_train,epochs=50,batch_size=16,shuffle=False)
predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(y_test)
real_price = scaler.inverse_transform(y_test)
print(predicted_price)

plt.figure(figsize=(20,8))
plt.plot(predicted_price,color="red",label="predicted price")
plt.plot(real_price,color="blue",label="Real Price")
plt.title("prediction vs Real")
plt.xlabel("time")
plt.ylabel("price")
plt.show()

# plt.figure(figsize=(20,8))
# plt.plot(predicted_price,color="red",label="predicted price")
# #plt.plot(real_price,color="blue",label="Real Price")
# plt.title("prediction vs Real")
# plt.xlabel("time")
# plt.ylabel("price")
# plt.show()
