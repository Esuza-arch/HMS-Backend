from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Doctor, Patient, Appointment, Review 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)
migrate = Migrate(app, db)

app.route('/')
def home():
    return jsonify({"message": "Welcome to the Hospital Management System API"})

 
    
if __name__ == '__main__':
    app.run(debug=True, port=5555)