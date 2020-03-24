from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        student = request.form['student']
        matric_number = request.form['matric_number']
        mahallah = request.form['mahallah']
        rating = request.form['rating']
        comments = request.form['comments']
        #print(student, matric_number, mahallah, rating, comments)
        if student == '' or matric_number == '' or mahallah == '':
            return render_template('index.html', message= 'Please enter the details')
        return render_template('success.html')


if __name__ == '__main__' :
    app.run(debug=True)