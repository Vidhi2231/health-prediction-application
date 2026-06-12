from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional


class PatientBase(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)

    email: EmailStr

    dob: date

    glucose: float

    haemoglobin: float

    cholesterol: float


class PatientCreate(PatientBase):
    pass


class PatientUpdate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    remarks: Optional[str] = None

    class Config:
        from_attributes = True