from pandas_datareader import data as pdr
import datetime as dt
import pickle

# yf.pdr_override()

end_date = dt.datetime.today()
start_date = end_date - dt.timedelta(days=25)
bitcoin = pdr.get_data_yahoo('BTC-USD', start_date, end_date)
bitcoin.drop(columns='Adj Close', inplace=True)
len(bitcoin)
required_features = ['Open', 'High', 'Low', 'Volume']
future_set = bitcoin.shift(periods=0)
print(future_set)


pklmodel = pickle.load(open('test.pkl','rb'))
prediction = pklmodel.predict(future_set[required_features])
print(prediction)