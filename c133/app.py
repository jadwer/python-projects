from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_flask():
    return "Este es mi primer programa en Flask"

@app.route("/flask_2")
def second_flask():
    return "¡Python es divertido!"

app.run(debug=True)