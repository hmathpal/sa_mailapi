import sentry_sdk
from flask import Flask, jsonify, request
from mail import send_simple_message, send_template_message

# Initialize Sentry
sentry_sdk.init(
    dsn="https://f45a9e728ffafbb05e12f69ae43d3444@o4507867663499264.ingest.us.sentry.io/4507867664744448",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.before_request
def log_request_info():
    # Log request details before handling the request
    if request.endpoint == 'api_send':
        app.logger.info(f"Request to /api/email: Method: {request.method}, URL: {request.url}, Headers: {dict(request.headers)}, Body: {request.get_data(as_text=True)}")

@app.after_request
def log_response_info(response):
    # Log response details after handling the request
    if request.endpoint == 'api_send':
        app.logger.info(f"Response from /api/email: Status: {response.status}, Body: {response.get_data(as_text=True)}")
    return response

@app.route("/")
def hello_world():
    1 / 0  # raises an error to test Sentry
    return "<p>Hello, World!</p>"

@app.route('/api/email', methods=['POST'])
def api_send():
    # Get JSON data from the request
    data = request.json
    
    # Log the request data
    sentry_sdk.capture_message(f"Request Data: {data}")

    # Extract required parameters and validate
    reciever_name = data.get('reciever_name')
    reciever_email = data.get('reciever_email')
    email_subject = data.get('email_subject')

    content_block_1 = data.get('content_block_1')
    content_block_2 = data.get('content_block_2')
    content_block_3 = data.get('content_block_3')

    attachment = data.get('attachment', None)  # Optional parameter
    img_url = data.get('img_url', None)

    # Validate that all required parameters are provided
    if not reciever_name or not reciever_email or not email_subject:
        error_message = 'Missing required parameters: reciever_name, reciever_email, and email_subject'
        sentry_sdk.capture_message(error_message)
        return jsonify({'error': error_message}), 400
    
    # Validate that at least one content block is provided
    if not content_block_1 or not content_block_2 or not content_block_3:
        error_message = 'Missing required parameters: content_block1, content_block2, content_block3'
        sentry_sdk.capture_message(error_message)
        return jsonify({'error': error_message}), 400

    # Call the function to send the message
    response = send_simple_message(reciever_name, img_url, reciever_email, email_subject, content_block_1, content_block_2, content_block_3, attachment)
    
    # Create a response
    response_data = {
        'status': response.status_code,
        'received_message': response.text,
        'attachment': attachment
    }

    # Log the response data
    sentry_sdk.capture_message(f"Response Data: {response_data}")

    return jsonify(response_data)

@app.route('/api/emailt', methods=['POST'])
def api_tsend():
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
    img_url = data.get('img_url', None)

    # Validate that all required parameters are provided
    if not reciever_name or not reciever_email or not email_subject:
        return jsonify({'error': 'Missing required parameters: reciever_name, reciever_email, and email_subject'}), 400
    
    # Validate that at least one content block is provided
    if not content_block_1 or not content_block_2 or not content_block_3:
        return jsonify({'error': 'Missing required parameters: content_block1, content_block2, content_block3 '}), 400

    # Call the function to send the message
    response = send_template_message(reciever_name, reciever_email, email_subject)
    
    # Create a response
    response_data = {
        'status': response.status_code,
        'received_message': response.text,
        'attachment': attachment
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
