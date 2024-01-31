from flask import Flask, request, jsonify
from pytryfi import PyTryFi
import os

app = Flask(__name__) 
USERNAME = os.getenv('PYTRYFI_USERNAME')
PASSWORD = os.getenv('PYTRYFI_PASSWORD')

@app.route('/')
def hello():
	return "Hello World!"

# /steps?days=30
@app.route('/steps', methods=['GET'])
def get_steps():
    # Get the 'days' parameter from the query string
    days_param = request.args.get('days')

    # Check if 'days' parameter is provided and is a valid integer
    if days_param is None or not days_param.isdigit():
        #return jsonify({'error': 'Invalid or missing "days" parameter'}), 400
        days_param = 14

    # Convert 'days' parameter to an integer
    days = int(days_param)

    tryfi = PyTryFi(USERNAME, PASSWORD)
    tryfi.pets[0].updateHistoricalStepStats(tryfi.session, days=days)

    data = tryfi.pets[0].stepsByDay
    
    # Create a JSON response
    response_data = {
        'data': data
    }


    return jsonify(response_data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)