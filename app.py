from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory leaderboard (resets on server restart)
leaderboard_data = []

@app.route('/')
def home():
    return render_template('index.html')

# Route to Save Score (No Database)
@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    player_name = data.get("player_name")
    score = data.get("score")

    # Add score to leaderboard
    leaderboard_data.append({"player_name": player_name, "score": score})

    # Keep only top 5 scores
    leaderboard_data.sort(key=lambda x: x["score"], reverse=True)  # Sort by score (descending)
    leaderboard_data[:] = leaderboard_data[:5]  # Keep only top 5

    return jsonify({"message": "Score saved!"})

# Route to Get Top 5 Scores
@app.route('/leaderboard')
def leaderboard():
    return jsonify(leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)
