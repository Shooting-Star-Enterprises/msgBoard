from flask import Flask, request, jsonify
from collections import deque

app = Flask(__name__)

# Define a deque to store messages (max 100 messages)
messages = deque(maxlen=1000)

# Route for posting a message
@app.route('/post_message', methods=['POST'])
def post_message():
    data = request.get_json()

    username = data.get('username')
    message = data.get('message')

    if not username or not message:
        return jsonify({'error': 'Username and message cannot be empty'}), 400

    messages.append({'username': username, 'message': message})
    return jsonify({'status': 'Message posted successfully'}), 201

# Route for getting last n messages
@app.route('/get_messages', methods=['GET'])
def get_messages():
    n = int(request.args.get('n', 10))  # Default value of n is 10

    if n < 1:
        return jsonify({'error': 'Invalid value of n'}), 400

    if n > len(messages):
       n = len(messages)

    last_n_messages = list(messages)[-n:]
    return jsonify({'messages': last_n_messages}), 200

if __name__ == '__main__':
    app.run(debug=True)

