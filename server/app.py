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

@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([doctors.dict() for doctor in doctors])

@app.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({"message": "Doctor not found"}), 404
    return jsonify(doctor.dict())

@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.json
    doctor = Doctor(name=data['name'], specialty=data['specialty'], experience=data['experience'])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(doctor.dict()), 201

@app.route('/doctors/<int:id>', methods=['PATCH'])
def update_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404
    
    data = request.json
    doctor.name = data.get('name', doctor.name)
    doctor.specialty = data.get('specialty', doctor.specialty)
    doctor.experience = data.get('experience', doctor.experience)

    db.session.commit()
    return jsonify(doctor.to_dict())

@app.route('/doctors/<int:id>', methods=['DELETE'])
def delete_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404
    
    db.session.delete(doctor)
    db.session.commit()
    return jsonify({"message": "Doctor deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5555)