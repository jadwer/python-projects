from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/index")
def first_webpage():
    name = 'Flask'
    my_var = 'Otra variable'
    image = url_for('static', filename='1.png')
    return render_template('index.html', index_variable=name, myvar = my_var, image=image)

app.run(debug=True)
