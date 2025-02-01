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

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Hospital Management System API"})

@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([doctor.to_dict() for doctor in doctors])

@app.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({"message": "Doctor not found"}), 404
    return jsonify(doctor.to_dict())

@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.json
    new_doctor = Doctor(name=data['name'], specialty=data['specialty'], experience=data['experience'])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(new_doctor.to_dict()), 201

@app.route('/doctors/<int:id>', methods=['PATCH'])
def update_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({"message": "Doctor not found"}), 404
    
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

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])

@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient.to_dict())

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    new_patient = Patient(name=data['name'], email=data['email'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify(new_patient.to_dict()), 201

@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments])

@app.route('/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify(appointment.to_dict())

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    try:
        appointment = Appointment(
            doctor_id=data['doctor_id'],
            patient_id=data['patient_id'],
            date=data['date'],
            time=data['time'],
            reason=data['reason']
        )
        db.session.add(appointment)
        db.session.commit()
        return jsonify(appointment.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/appointments/<int:id>', methods=['PATCH'])
def update_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    
    data = request.json
    appointment.doctor_id = data.get('doctor_id', appointment.doctor_id)
    appointment.patient_id = data.get('patient_id', appointment.patient_id)
    appointment.date = data.get('date', appointment.date)
    appointment.time = data.get('time', appointment.time)
    appointment.reason = data.get('reason', appointment.reason)

    db.session.commit()
    return jsonify(appointment.to_dict())

@app.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    
    db.session.delete(appointment)
    db.session.commit()
    return jsonify({"message": "Appointment deleted successfully"})   

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])

@app.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict())

@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    try:
        review = Review(
            doctor_id=data['doctor_id'],
            patient_id=data['patient_id'],
            rating=data['rating'],
            comment=data['comment']
        )
        db.session.add(review)
        db.session.commit()
        return jsonify(review.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully"})     



if __name__ == '__main__':
    app.run(debug=True, port=5555)