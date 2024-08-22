from flask import Flask, jsonify, request
from mail import send_simple_message

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api_hello():
    return jsonify(message='Hello, World from API!')




from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def api_send():
    # Get JSON data from the request
    data = request.json
    
    # Extract required parameters and validate
    reciever_name = data.get('reciever_name')
    reciever_email = data.get('reciever_email')
    email_subject = data.get('email_subject')

    content_block_1 = data.get('content_block_1')
    content_block_2 = data.get('content_block_2')
    content_block_3 = data.get('content_block_3')

    attachment = data.get('attachment', None)  # Optional parameter

    # Validate that all required parameters are provided
    if not reciever_name or not reciever_email or not email_subject:
        return jsonify({'error': 'Missing required parameters: reciever_name, reciever_email, and email_subject'}), 400
    
    # Validate that at least one content block is provided
    if not content_block_1 or not content_block_2 or not content_block_3:
        return jsonify({'error': 'Missing required parameters: content_block1, content_block2, content_block3 '}), 400

    
    # Call the function to send the message
    print("Calling send_simple_message function")
    response = send_simple_message(reciever_name, reciever_email, email_subject, content_block_1, content_block_2, content_block_3, attachment)
    
    # Create a response
    response = {
        'status': response.status_code,
        'received_message': response.text,
        'attachment': attachment
    }
    
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)


