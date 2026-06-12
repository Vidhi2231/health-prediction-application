from sqlalchemy.orm import Session

import models
import schemas


def create_patient(
    db: Session,
    patient: schemas.PatientCreate,
    remarks: str
):

    db_patient = models.Patient(
        full_name=patient.full_name,
        email=patient.email,
        dob=patient.dob,
        glucose=patient.glucose,
        haemoglobin=patient.haemoglobin,
        cholesterol=patient.cholesterol,
        remarks=remarks
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def get_patients(
    db: Session
):
    return db.query(models.Patient).all()


def get_patient(
    db: Session,
    patient_id: int
):
    return (
        db.query(models.Patient)
        .filter(models.Patient.id == patient_id)
        .first()
    )


def update_patient(
    db: Session,
    patient_id: int,
    patient: schemas.PatientUpdate,
    remarks: str
):

    db_patient = get_patient(
        db,
        patient_id
    )

    if not db_patient:
        return None

    db_patient.full_name = patient.full_name
    db_patient.email = patient.email
    db_patient.dob = patient.dob

    db_patient.glucose = patient.glucose
    db_patient.haemoglobin = patient.haemoglobin
    db_patient.cholesterol = patient.cholesterol

    db_patient.remarks = remarks

    db.commit()
    db.refresh(db_patient)

    return db_patient


def delete_patient(
    db: Session,
    patient_id: int
):

    db_patient = get_patient(
        db,
        patient_id
    )

    if not db_patient:
        return False

    db.delete(db_patient)

    db.commit()

    return True