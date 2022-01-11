from flask import Flask, request
from model import result

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():
    request_data = request.get_json()
		
    crypto = request_data["crypto"]
    days = request_data["days"]
    value = result(crypto+"USD", days)
    print(value)
    response_body = value
    return response_body


if __name__ == '__main__':
    app.run()












