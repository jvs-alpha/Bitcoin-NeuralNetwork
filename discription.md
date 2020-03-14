# Bitcoin Closeing price prediction using RNN (Long-Short-Term-Memory)

## Modules Used

### Getting the data from the Websited
* urllib
* json
* csv
* datetime
* binance

### Refining the Data
* pandas
* numpy
* sklearn

### Neural Network Modules
* tensorflow with keras


## Module Uses

### Urllib
 This python module is used for sending and receiving the HTTP request over the internet
 like GET,POST,DELETE etc. We are using the request function to send GET request
 to receive data as a json format which is the universal format for getting data over the HTTP
 we then send the data to the json module for converting to python processable format like dictionary

### Json
This module is used for converting the JSON data that is received from a HTTP GET Request or REST API
to a python readable format like the dictionay which has similar syntax like the JSON format data
Here we are using it to convert the raw JSON data from poloniex website to python fromat for processing

### CSV
The CSV is the abbrivation for "Comma Seperated Variables". The csv module used in python for reading
CSV files or to write to a CSV file. Here we are using the csv module in python for storing the data
from poloniex

### Datetime
The datetime module is used in python for dealing with the date and time.
This module can be used for converting a timestamp to YYYY-MM-DD HH:MM:SS format
for processing with the Neural Network

### Binance
This is a proprietary module which is used for getting the data from the binance website using their APIKey
and the SecretKey. Here we are using as out backup data retriving for model testing purpose

### Pandas
The pandas library is used for data science and data processing.
This uses the numpy objects as the inputing the data and matplotlib.pyplot for
visualization of the data. This converts the numpy.ndarray into a pnadas.dataframe
to process the data which given as the input

### Numpy
The Numpy is a mathematical library for creating and fast processing of n-dimention data.
We have other mathematical prcessing library in python but we have chosen Numpy becoz it
is compatible with most of the ML libraried and also it more faster to compute data in
Numpy lib then the treditional list and array of the python

### Sklearn
The Sklearn is a ML library of its own but here we are using it for preprocessing of the data
which means the data that we have here is in a broad range of data which is very hard for
Neural Network to process so we bring down the range of the data to a certain constraint range
ideally in between 0 and 1. We are using the Scaleing function for converting the data
to 0 to 1 range using the Sigmoid method

### Tensorflow and Keras
The Tensorflow is the mechine learning library that we are using for training or model
the 
