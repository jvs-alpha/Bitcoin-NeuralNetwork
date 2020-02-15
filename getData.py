from urllib import request
import json
import datetime
import csv

site = "https://poloniex.com/public?command=returnChartData&currencyPair=USDC_BTC&start=1420070400&end=15816986170&period=14400&depth=10"
rawdata = request.urlopen(site)
jsondata = json.load(rawdata)
with open("data.csv","w") as csvfile:
    fieldnames = ["date","high","low","open","close","volume","quoteVolume","weightedAverage"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    
    for i in jsondata:
        date = datetime.datetime.fromtimestamp(i["date"])
        high = i["high"]
        low = i["low"]
        open = i["open"]
        close = i["close"]
        volume = i["volume"]
        quoteVolume = i["quoteVolume"]
        weightedAverage = i["weightedAverage"]
        writer.writerow({"date":date,"high":high,"low":low,"open":open,"close":close,"volume":volume,"quoteVolume":quoteVolume,"weightedAverage":weightedAverage})
        print("Date: {}\nHigh: {}\nLow: {}\nOpen: {}\nClose: {}\nVolume: {}\nQuoteVolume: {}\nWeightedAverage: {}".format(date,high,low,open,close,volume,quoteVolume,weightedAverage))
        print()
