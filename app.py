from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Very simple way to store the latest score in memory
# For a real application you might want to use a database and player IDs
latest_score = 0

@app.route('/')
def home():
    # Render the game directly on the home route
    return render_template('space_invaders.html')

@app.route('/api/score', methods=['GET'])
def get_score():
    return jsonify({"score": latest_score})

@app.route('/api/score', methods=['POST'])
def save_score():
    global latest_score
    data = request.get_json()
    if data and 'score' in data:
        latest_score = data['score']
        return jsonify({"status": "success", "score": latest_score})
    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
