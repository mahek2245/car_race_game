from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password="2245",  # Change this to your MySQL password
    database="car_race_game"
)
cursor = db.cursor()

# Route for Game Page
@app.route('/')
def home():
    return render_template('index.html')

# Route to Save Score in Database
@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    player_name = data.get("player_name")
    score = data.get("score")

    query = "INSERT INTO scores (player_name, score) VALUES (%s, %s)"
    cursor.execute(query, (player_name, score))
    db.commit()
    
    return jsonify({"message": "Score saved!"})

# Route to Get Top 5 Scores
@app.route('/leaderboard')
def leaderboard():
    cursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 5")
    top_scores = cursor.fetchall()
    return jsonify(top_scores)

if __name__ == '__main__':
    app.run(debug=True)
