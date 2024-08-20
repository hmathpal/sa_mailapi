from flask import Flask, jsonify, request
from mail import send_simple_message

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api_hello():
    return jsonify(message='Hello, World from API!')



@app.route('/api/send', methods=['POST'])
def api_send():
    # Get JSON data from the request
    data = request.json
    
    # Process the data (you can customize this part based on your needs)
    message = data.get('message', 'No message provided')
    
    response = send_simple_message()
    # Create a response
    response = {
        'status': response.text,
        'received_message': message
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
