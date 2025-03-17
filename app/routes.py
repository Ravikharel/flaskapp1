from app import app, db
from flask import jsonify

@app.route('/')
def index():
    return jsonify(message="Hello, Flask and MySQL are connected!")

@app.route('/initdb')
def init_db():
    with app.app_context():
        db.create_all()
    return jsonify(message="Database initialized!")
