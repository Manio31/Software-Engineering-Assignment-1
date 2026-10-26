from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
                                                
def create_table():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify({
        "message": "Student Management API is running!"
    })

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required_fields = ["name", "department", "email"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()

    cursor = conn.execute(
        """UPDATE students
           SET name = ?, department = ?, email = ?
           WHERE id = ?""",
        (
            data["name"],
            data["department"],
            data["email"],
            student_id
        )
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully"})


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required_fields = ["id", "name", "department", "email"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()

    try:
        conn.execute(
            """INSERT INTO students (id, name, department, email)
               VALUES (?, ?, ?, ?)""",
            (
                data["id"],
                data["name"],
                data["department"],
                data["email"]
            )
        )

        conn.commit()
                                    
    except sqlite3.IntegrityError:
        return jsonify({"error": "Student ID already exists"}), 409

    finally:
        conn.close()
                        
    return jsonify({
        "message": "Student added successfully"
    }), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = get_db_connection()

    cursor = conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Student deleted successfully"
    })

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
