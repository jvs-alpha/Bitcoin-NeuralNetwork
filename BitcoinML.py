from keys import *
import datetime
from binance.client import Client
import matplotlib.pyplot as plt
import pandas as pd
client = Client(APIKey,SecretKey)
symbol = "BTCUSDT"
BTC = client.get_historical_klines(symbol=symbol,interval=Client.KLINE_INTERVAL_30MINUTE,start_str="1 year ago UTC")
BTC = pd.DataFrame(BTC,columns=["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume","Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"])
BTC["Open time"] = pd.to_datetime(BTC["Open time"],unit="ms")
BTC.set_index("Open time",inplace=True)
BTC["Close"] = BTC["Close"].astype(float)
BTC["Close"].plot(figsize=(20,10),title="1 year")
plt.show()
