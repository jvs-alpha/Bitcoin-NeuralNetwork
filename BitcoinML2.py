import pandas as pd
from keys import *
from binance.client import Client
from sklearn.preprocessing import MinMaxScaler


# dataset = pd.read_csv("data.csv")

client = Client(APIKey,SecretKey)
symbol = "BTCUSDT"
BTC = client.get_historical_klines(symbol=symbol,interval=Client.KLINE_INTERVAL_30MINUTE,start_str="1 year ago UTC")
BTC = pd.DataFrame(BTC,columns=["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume","Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"])
BTC["Open time"] = pd.to_datetime(BTC["Open time"],unit="ms")
BTC.set_index("Open time",inplace=True)
BTC["Close"] = BTC["Close"].astype("float")
data = BTC.iloc[:,[3]].astype("float").values
scaler = MinMaxScaler()
data = scaler.fit_transform(data)
training_set = data[0:len(data)-1]
print(len(training_set))
