from urllib import request
import json
import datetime

site = "https://poloniex.com/public?command=returnChartData&currencyPair=USDC_BTC&start=1420070400&end=15816986170&period=14400"
rawdata = request.urlopen(site)
jsondata = json.load(rawdata)
check = 0
for i in jsondata:
    check += 1
    date = datetime.datetime.fromtimestamp(i["date"])
    print(date)
print(check)
