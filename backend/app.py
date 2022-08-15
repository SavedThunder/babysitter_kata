from wsgiref.handlers import format_date_time
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from calculate_charge import calculate_nightly_charge, format_times
from datetime import datetime


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

@app.route("/hello_world")
def hello_world():
    return "Hello World!!!"

@app.route("/calculate_balance", methods=['POST'])
def calculate_balance():
    args = request.get_json(force=True)
    print(args)

    start_time = format_times(args.get('start_time'))
    end_time = format_times(args.get('end_time'))
    bed_time = format_times(args.get('bed_time'))
    
    print(start_time, end_time, bed_time)
    calculation = calculate_nightly_charge(start_time, end_time, bed_time)
    return jsonify(calculation)


if __name__ == '__main__':
    app.run()
