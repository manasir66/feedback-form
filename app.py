from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from send_mail import send_mail

app = Flask(__name__)


ENV = 'prod' #production

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ' '
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key= True)
    student = db.Column(db.String(200), unique=True)
    matric_number = db.Column(db.Integer, unique=True)
    mahallah = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, student, matric_number, mahallah, rating, comments):
        self.student = student
        self.matric_number = matric_number
        self.mahallah = mahallah
        self.rating = rating
        self.comments = comments


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
        
        if db.session.query(Feedback).filter(Feedback.student == student).count() == 0 :
            data =  Feedback(student, matric_number, mahallah, rating, comments)
            db.session.add(data)
            db.session.commit()

            send_mail(student, matric_number, mahallah, rating, comments)

            return render_template('success.html')
        
        return render_template('index.hml', message='You have already submitted feedback')


if __name__ == '__main__' :
    app.run(debug=True)
