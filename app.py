from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Sam", "branch": "CSE"},
    {"id": 2, "name": "Rahul", "branch": "ECE"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/')
def home():
    return "CircleCI Application Running!"

if __name__ == '__main__':
    app.run(debug=True)