from urllib import request
import json
import datetime

site = "https://poloniex.com/public?command=returnChartData&currencyPair=USDC_BTC&start=1420070400&end=15816986170&period=14400&depth=10"
rawdata = request.urlopen(site)
jsondata = json.load(rawdata)
check = 0
for i in jsondata:
    if check == 10:
        break
    date = datetime.datetime.fromtimestamp(i["date"])
    high = i["high"]
    low = i["low"]
    open = i["open"]
    close = i["close"]
    volume = i["volume"]
    quotevolume = i["quoteVolume"]
    weightedaverage = i["weightedAverage"]
    print("Date: {}\nHigh: {}\nLow: {}\nOpen: {}\nClose: {}\nVolume: {}\nQuoteVolume: {}\nWeightedAverage: {}".format(date,high,low,open,close,volume,quotevolume,weightedaverage))
    print()
    check += 1
