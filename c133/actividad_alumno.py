from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first_flask():
    return "Este es mi primer programa en Flask"

@app.route("/actividad_alumno")
def student_webpage():
    name = 'John'
    return render_template('student.html', student_name = name)

app.run(debug=True)