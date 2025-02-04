from faker import Faker
from server.models import db, Doctor, Patient, Appointment, Review
from app import app
import random
from datetime import datetime, timedelta

faker = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create fake doctors
    doctors = [Doctor(name=faker.name(), specialty=faker.job(), experience=random.randint(1, 30)) for _ in range(5)]
    db.session.add_all(doctors)
    db.session.commit()

    # Create fake patients
    patients = [Patient(name=faker.name(), email=faker.email()) for _ in range(10)]
    db.session.add_all(patients)
    db.session.commit()

    # Create fake appointments
    for _ in range(15):
        appointment = Appointment(
            doctor_id=random.choice(doctors).id,
            patient_id=random.choice(patients).id,
            date=faker.date_between(start_date="-30d", end_date="today"),
            time=faker.time_object(),
            reason=faker.sentence()
        )
        db.session.add(appointment)

    db.session.commit()

    # Create fake reviews
    for _ in range(10):
        review = Review(
            doctor_id=random.choice(doctors).id,
            patient_id=random.choice(patients).id,
            rating=random.randint(1, 5),
            comment=faker.sentence()
        )
        db.session.add(review)

    db.session.commit()

    print("Database seeded successfully!")
