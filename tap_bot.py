from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Track coins for each user session
user_coins = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tap', methods=['POST'])
def tap():
    user_id = request.remote_addr  # Use IP address as a simple user identifier
    user_coins[user_id] = user_coins.get(user_id, 0) + 1  # Increment coin count
    return jsonify({'coins': user_coins[user_id]})

@app.route('/coins', methods=['GET'])
def coins():
    user_id = request.remote_addr
    return jsonify({'coins': user_coins.get(user_id, 0)})

if __name__ == "__main__":
    app.run(debug=True)
