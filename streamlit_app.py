
import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="Student Management System",
    layout="wide"
)

st.title("Student Management System")
st.write("Manage student records using the Flask API.")


def get_students():
    try:
        response = requests.get(f"{API_URL}/students")
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        st.error("Could not connect to Flask API. Start app.py first.")
        return None


st.subheader("All Students")

students = get_students()

if students is not None:
    if students:
        st.dataframe(pd.DataFrame(students), use_container_width=True)
    else:
        st.info("No student records found.")

if st.button("Refresh Records"):
    st.rerun()

st.divider()
st.subheader("Add Student")

with st.form("add_student"):
    student_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    submitted = st.form_submit_button("Add Student")

    if submitted:
        if not name.strip() or not department.strip() or not email.strip():
            st.error("Please fill in all fields.")
        else:
            payload = {
                "id": int(student_id),
                "name": name.strip(),
                "department": department.strip(),
                "email": email.strip()
            }

            try:
                response = requests.post(
                    f"{API_URL}/students",
                    json=payload
                )

                if response.status_code == 201:
                    st.success("Student added successfully!")
                    st.rerun()
                else:
                    st.error(response.json().get("error", "Unable to add student."))
            except requests.RequestException:
                st.error("Could not connect to Flask API.")

st.divider()
st.subheader("Update Student")

with st.form("update_student"):
    update_id = st.number_input(
        "Student ID to Update", min_value=1, step=1, key="update_id"
    )
    new_name = st.text_input("New Name")
    new_department = st.text_input("New Department")
    new_email = st.text_input("New Email")

    update_submitted = st.form_submit_button("Update Student")

    if update_submitted:
        if not new_name.strip() or not new_department.strip() or not new_email.strip():
            st.error("Please fill in all fields.")
        else:
            payload = {
                "name": new_name.strip(),
                "department": new_department.strip(),
                "email": new_email.strip()
            }

            try:
                response = requests.put(
                    f"{API_URL}/students/{int(update_id)}",
                    json=payload
                )

                if response.status_code == 200:
                    st.success("Student updated successfully!")
                    st.rerun()
                else:
                    st.error(response.json().get("error", "Unable to update student."))
            except requests.RequestException:
                st.error("Could not connect to Flask API.")

st.divider()
st.subheader("Delete Student")

with st.form("delete_student"):
    delete_id = st.number_input(
        "Student ID to Delete", min_value=1, step=1, key="delete_id"
    )

    delete_submitted = st.form_submit_button("Delete Student")

    if delete_submitted:
        try:
            response = requests.delete(
                f"{API_URL}/students/{int(delete_id)}"
            )

            if response.status_code == 200:
                st.success("Student deleted successfully!")
                st.rerun()
            else:
                st.error(response.json().get("error", "Unable to delete student."))
        except requests.RequestException:
            st.error("Could not connect to Flask API.")
