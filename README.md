# Task 1: Database-Driven Student Management API

## Project Overview
This project is a Student Management System developed using Flask, SQLite, and Streamlit. It provides REST API endpoints to add, view, update, and delete student records. The Streamlit interface allows users to manage student data through a simple graphical interface.

## Technologies Used
- Python
- Flask
- SQLite
- Streamlit
- Requests
- Pandas
- Visual Studio Code

## Features
- View all students
- View a specific student by ID
- Add a new student
- Update existing student information
- Delete a student record
- Display student records in a table
- Refresh the student list through the interface

## Project Structure
```text
Task_1_Database_API_StreamLit/
    streamlit_app.py
    README.md
    requirements.txt

app.py
students.db
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/<id>` | Retrieve a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

## Installation and Setup

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder
Open the downloaded project folder in Visual Studio Code.

### 3. Install Dependencies
Activate your virtual environment, then run:

```bash
pip install -r requirements.txt
```

### 4. Start the Flask API
Run the following command from the project root folder:

```bash
python app.py
```

The API will run at:

`http://127.0.0.1:5000`

### 5. Start the Streamlit Interface
Open a second terminal and run:

```bash
python -m streamlit run Task_1_Database_API_StreamLit/streamlit_app.py
```

The Streamlit interface will open in your browser, usually at:

`http://localhost:8501`

## Testing
The API can be tested using a browser for GET requests and tools such as Postman or PowerShell for POST, PUT, and DELETE requests. The Streamlit interface can also be used to add, view, update, and delete student records.

## Demo Video
The project demonstration video will show the working API and the Streamlit interface, including student creation, viewing, updating, and deletion.

**Demo Video:** https://youtu.be/a8-3bCTTTiI?si=AtqFnt1NwKNJOpDp

## Author
Abdul Manio Hulio
BS Computer Science
Computer Science Student  
SZABIST University, Larkana

## Academic Project
Developed as part of the Software Engineering assignment on developing custom APIs for microservices.
