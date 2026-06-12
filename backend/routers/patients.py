from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

import schemas
import crud

from database import get_db
from ai_service import generate_ai_remark

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post(
    "/",
    response_model=schemas.PatientResponse
)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db)
):

    if patient.dob > date.today():
        raise HTTPException(
            status_code=400,
            detail="DOB cannot be a future date"
        )

    remarks = generate_ai_remark(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )

    return crud.create_patient(
        db,
        patient,
        remarks
    )


@router.get(
    "/",
    response_model=list[schemas.PatientResponse]
)
def get_all_patients(
    db: Session = Depends(get_db)
):

    return crud.get_patients(db)


@router.get(
    "/{patient_id}",
    response_model=schemas.PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = crud.get_patient(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@router.put(
    "/{patient_id}",
    response_model=schemas.PatientResponse
)
def update_patient(
    patient_id: int,
    patient: schemas.PatientUpdate,
    db: Session = Depends(get_db)
):

    if patient.dob > date.today():
        raise HTTPException(
            status_code=400,
            detail="DOB cannot be future date"
        )

    remarks = generate_ai_remark(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )

    updated = crud.update_patient(
        db,
        patient_id,
        patient,
        remarks
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return updated


@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_patient(
        db,
        patient_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }