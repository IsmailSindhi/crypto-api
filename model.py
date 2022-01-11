import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pandas_datareader import data as pdr
import datetime as dt
import pickle

yf.pdr_override()

# BTC-USD

end_date = dt.datetime.today()
start_date = end_date - dt.timedelta(days=120)
bitcoin = pdr.get_data_yahoo('BTC-USD', start_date, end_date)
bitcoin.drop(columns='Adj Close', inplace=True)
required_features = ['Open', 'High', 'Low', 'Volume']
output_label = 'Close'
x_train, x_test, y_train, y_test = train_test_split(
bitcoin[required_features],
bitcoin[output_label],
test_size = 0.3)
model = LinearRegression()
model.fit(x_train, y_train)
pickle.dump(model, open('test.pkl','wb'))
# pklmodel = pickle.load(open('test.pkl','rb')
# future_set = bitcoin.shift(periods=7)
# prediction = pklmodel.predict(future_set[required_features])
# # return prediction[days]
# # pickle.load(open('model.pkl','rb'))
# # print(result('ETH-USD',15))
