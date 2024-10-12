from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

# Database connection setup
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="12345678",  # Replace with your correct password
    db="student_db"
)

@app.route('/')
def index():
    return render_template('result.html')

@app.route('/result', methods=['POST'])
def result():
    roll_number = request.form['roll_number']
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM results WHERE roll_number = %s", (roll_number,))
    result = cursor.fetchone()

    if result:
        student_data = {
            'roll_number': result[0],
            'student_name': result[1],
            'subject1': result[2],
            'subject2': result[3],
            'subject3': result[4],
            'total': result[5]
        }
        # Render the results in a structured format
        return render_template('result_display.html', student_data=student_data)
    else:
        return "No result found for the entered roll number."

if __name__ == '__main__':
    app.run(debug=True)
