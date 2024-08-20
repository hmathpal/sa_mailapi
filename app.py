from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api_hello():
    return jsonify(message='Hello, World from API!')

if __name__ == '__main__':
    app.run(debug=True)
