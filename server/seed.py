from models import db, Doctor, Patient, Appointment, Review
from app import app
from datetime import date, time

with app.app_context():
    db.drop_all()
    db.create_all()

    doctor1 = Doctor(name="Dr. Smith", specialty="Cardiology", experience=10)
    doctor2 = Doctor(name="Dr. Adams", specialty="Neurology", experience=8)

    patient1 = Patient(name="John Doe", email="johndoe@example.com")
    patient2 = Patient(name="Jane Smith", email="janesmith@example.com")

    appointment1 = Appointment(doctor_id=1, patient_id=1, date=date(2025, 2, 1), time=time(10, 0), reason="Regular check-up")
    appointment2 = Appointment(doctor_id=2, patient_id=2, date=date(2025, 2, 3), time=time(14, 30), reason="Headache consultation")

    review1 = Review(doctor_id=1, patient_id=1, rating=5, comment="Great service!")
    review2 = Review(doctor_id=2, patient_id=2, rating=4, comment="Very helpful")
    
    db.session.add_all([doctor1, doctor2, patient1, patient2, appointment1, appointment2, review1, review2])
    db.session.commit()