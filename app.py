from flask import Flask, request, jsonify
from model import result

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
        request_data = request.get_json()
        print(request_data)
        crypto = request_data["crypto"]
        days = request_data["days"]
        print(crypto)
        print(days)
        value = result(crypto,days)
        response_body = {
            "currency" : crypto,
            "days" : days,
            "value": value
        }
        return response_body
if __name__ == '__main__':
    app.run()