# 🏥 Health Prediction Application

## Project Overview

Health Prediction Application is an AI-powered healthcare management system developed using FastAPI, Streamlit, SQLite, SQLAlchemy ORM, and OpenAI.

The application allows healthcare staff to manage patient blood test records and automatically generate health risk assessments based on blood test values.

The system supports complete CRUD functionality and AI-assisted health prediction.

---

## Features

### Patient Management

* Create Patient Record
* View Patient Records
* Update Patient Record
* Delete Patient Record

### Data Validation

* Valid Email Validation
* Date of Birth Validation
* Numeric Blood Test Validation

### Health Prediction

* Rule-Based Health Risk Analysis
* OpenAI-Powered Health Remarks
* Automatic Risk Assessment

### Database

* SQLite Database
* SQLAlchemy ORM
* Persistent Data Storage

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

### Frontend

* Streamlit
* Pandas

### AI Integration

* OpenAI API
* Rule-Based Prediction Engine

---

## Project Structure

HealthPrediction/

backend/

* main.py
* database.py
* models.py
* schemas.py
* crud.py
* ai_service.py
* routers/

frontend/

* app.py

.env
requirements.txt
README.md
DEMO_VIDEO_SCRIPT.md

---

## Installation

### Clone Repository

git clone <repository_url>

cd HealthPrediction

### Create Virtual Environment

python -m venv myenv

### Activate Environment

Windows:

myenv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Environment Configuration

Create a .env file:

OPENAI_API_KEY=your_api_key

---

## Run Backend

cd backend

uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs

---

## Run Frontend

cd frontend

streamlit run app.py

Frontend URL:

http://localhost:8501

---

## Sample Patient Data

Name: xyz

Email: [xyz@example.com]

DOB: 1995-05-10

Glucose: 180

Haemoglobin: 10

Cholesterol: 260

---

## Future Enhancements

* JWT Authentication
* Role-Based Access Control
* Machine Learning Model Training
* Cloud Deployment
* Docker Support
* Analytics Dashboard

---

## Author

Vidhi Dave 

AI Engineer

