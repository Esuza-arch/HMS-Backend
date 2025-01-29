from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Doctor(db.Model):
    __tablename__ = 'doctors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    appointments = db.relationship('Appointment', back_populates='doctor')
    reviews = db.relationship('Review', back_populates='doctor')

    def __repr__(self):
        return f"<Doctor {self.id}: {self.name}, Specialty: {self.specialty}, Experience: {self.experience} years>"

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)

    appointments = db.relationship('Appointment', back_populates='patient')
    reviews = db.relationship('Review', back_populates='patient')

    def __repr__(self):
        return f"<Patient {self.id}: {self.name}, Email: {self.email}>"
    
class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    reason = db.Column(db.String, nullable=False)

    doctor = db.relationship('Doctor', back_populates='appointments')
    patient = db.relationship('Patient', back_populates='appointments')

    def __repr__(self):
        return f"<Appointment {self.id}: Doctor: {self.doctor_id}, Patient: {self.patient_id}, Date: {self.date}>"

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=False)

    doctor = db.relationship('Doctor', back_populates='reviews')
    patient = db.relationship('Patient', back_populates='reviews')

    def __repr__(self):
        return f"<Review {self.id}: Doctor: {self.doctor_id}, Patient: {self.patient_id}, Rating: {self.rating}, Comment: {self.comment}>"