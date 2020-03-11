import keras.models
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

# Reading the data
BTC = pd.read_csv("data.csv",index_col=0)
BTC["close"] = BTC["close"].astype("float")
data = BTC.iloc[:,4].astype("float").values
data = np.reshape(data,(len(data),1))

# Normalizing the data
scaler = MinMaxScaler()
data = scaler.fit_transform(data)
data1 = np.reshape(data,(len(data),1,data.shape[1]))

# Loading the Model
model = keras.models.load_model("BTCPP.h5")

# Prediction of price
predicted_price = model.predict(data1)
predicted_price = scaler.inverse_transform(predicted_price)
real_price = scaler.inverse_transform(data)

# Visualization as a graph
plt.figure(figsize=(20,8))
plt.plot(predicted_price,color="red",label="Predicted price")
plt.plot(real_price,color="blue",label="Real Price")
plt.title("Prediction vs Real from 2019-10-10 09:30:00 to 2020-02-15 17:30:00")
plt.xlabel("time")
plt.ylabel("price")
plt.show()
