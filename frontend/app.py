import streamlit as st
import requests
import pandas as pd
from datetime import date

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Health Prediction System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Health Prediction Application")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Patient",
        "View Patients",
        "Update Patient",
        "Delete Patient"
    ]
)

# =====================================
# CREATE
# =====================================

if menu == "Create Patient":

    st.header("➕ Add New Patient")

    with st.form("create_form"):

        full_name = st.text_input("Full Name")

        email = st.text_input("Email Address")

        dob = st.date_input(
            "Date of Birth",
            max_value=date.today()
        )

        glucose = st.number_input(
            "Glucose",
            min_value=0.0
        )

        haemoglobin = st.number_input(
            "Haemoglobin",
            min_value=0.0
        )

        cholesterol = st.number_input(
            "Cholesterol",
            min_value=0.0
        )

        submit = st.form_submit_button("Create")

        if submit:

            payload = {
                "full_name": full_name,
                "email": email,
                "dob": str(dob),
                "glucose": glucose,
                "haemoglobin": haemoglobin,
                "cholesterol": cholesterol
            }

            try:

                response = requests.post(
                    f"{API_URL}/patients/",
                    json=payload
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        "Patient Created Successfully"
                    )

                    st.info(
                        f"AI Remark: {data['remarks']}"
                    )

                else:
                    st.error(response.text)

            except Exception as e:
                st.error(str(e))


# =====================================
# VIEW
# =====================================

elif menu == "View Patients":

    st.header("📋 Patient Records")

    try:

        response = requests.get(
            f"{API_URL}/patients/"
        )

        if response.status_code == 200:

            data = response.json()

            if data:

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    #use_container_width=True
                    width='stretch'
                )

            else:
                st.warning(
                    "No records found"
                )

        else:
            st.error(response.text)

    except Exception as e:
        st.error(str(e))


# =====================================
# UPDATE
# =====================================

elif menu == "Update Patient":

    st.header("✏️ Update Patient")

    try:

        response = requests.get(
            f"{API_URL}/patients/"
        )

        patients = response.json()

        if not patients:
            st.warning("No patients found")
            st.stop()

        patient_map = {
            f"{p['id']} - {p['full_name']}": p
            for p in patients
        }

        selected = st.selectbox(
            "Select Patient",
            list(patient_map.keys())
        )

        patient = patient_map[selected]

        with st.form("update_form"):

            full_name = st.text_input(
                "Full Name",
                value=patient["full_name"]
            )

            email = st.text_input(
                "Email",
                value=patient["email"]
            )

            dob = st.date_input(
                "DOB",
                value=pd.to_datetime(
                    patient["dob"]
                )
            )

            glucose = st.number_input(
                "Glucose",
                value=float(
                    patient["glucose"]
                )
            )

            haemoglobin = st.number_input(
                "Haemoglobin",
                value=float(
                    patient["haemoglobin"]
                )
            )

            cholesterol = st.number_input(
                "Cholesterol",
                value=float(
                    patient["cholesterol"]
                )
            )

            submit = st.form_submit_button(
                "Update"
            )

            if submit:

                payload = {
                    "full_name": full_name,
                    "email": email,
                    "dob": str(dob),
                    "glucose": glucose,
                    "haemoglobin": haemoglobin,
                    "cholesterol": cholesterol
                }

                response = requests.put(
                    f"{API_URL}/patients/{patient['id']}",
                    json=payload
                )

                if response.status_code == 200:

                    updated = response.json()

                    st.success(
                        "Patient Updated Successfully"
                    )

                    st.info(
                        f"New AI Remark: {updated['remarks']}"
                    )

                else:
                    st.error(response.text)

    except Exception as e:
        st.error(str(e))


# =====================================
# DELETE
# =====================================

elif menu == "Delete Patient":

    st.header("🗑 Delete Patient")

    try:

        response = requests.get(
            f"{API_URL}/patients/"
        )

        patients = response.json()

        if not patients:
            st.warning(
                "No patients found"
            )
            st.stop()

        patient_map = {
            f"{p['id']} - {p['full_name']}": p
            for p in patients
        }

        selected = st.selectbox(
            "Select Patient",
            list(patient_map.keys())
        )

        patient = patient_map[selected]

        st.write(
            f"Email: {patient['email']}"
        )

        st.write(
            f"Current Remark: {patient['remarks']}"
        )

        if st.button(
            "Delete Patient",
            type="primary"
        ):

            response = requests.delete(
                f"{API_URL}/patients/{patient['id']}"
            )

            if response.status_code == 200:

                st.success(
                    "Patient Deleted Successfully"
                )

            else:
                st.error(response.text)

    except Exception as e:
        st.error(str(e))