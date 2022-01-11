from flask import Flask, request
from model import value

app = Flask(__name__)


@app.route('/')
def home():
    if request.method == 'GET':
        response_body = {
            "value": "welcome to thinkfeat api"
        }
        return response_body

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        crypto = request.form["crypto"]
        days = request.form["days"]
        value = value(crypto, days)
        response_body = {
            "currency" : crypto,
            "days" : days,
            "value": value
        }
        return response_body
if __name__ == '__main__':
    app.run()












