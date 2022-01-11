from flask import Flask, request
import pickle
import yfinance as yf
from pandas_datareader import data as pdr
import datetime as dt

yf.pdr_override()

app = Flask(__name__)

end_date = dt.datetime.today()
start_date = end_date - dt.timedelta(days=120)
bitcoin = pdr.get_data_yahoo('BTC-USD', start_date, end_date)
bitcoin.drop(columns='Adj Close', inplace=True)
required_features = ['Open', 'High', 'Low', 'Volume']
future_set = bitcoin.shift(periods=4)

pklmodel = pickle.load(open('test.pkl','rb'))
prediction = pklmodel.predict(bitcoin[required_features])
print(prediction)
@app.route('/predict', methods = ['POST'])
def predict():
    request_data = request.get_json()		
    # crypto = request_data["crypto"]
    # days = request_data["days"]
    response_body = pklmodel.predict(bitcoin[required_features])
    return response_body


if __name__ == '__main__':
    app.run()












