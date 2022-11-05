from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prisma.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Something anonymous'

db = SQLAlchemy(app)

class Chairs(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    sell_price = db.Column(db.Integer)
    disc_price = db.Column(db.Integer)
    description = db.Column(db.String(1000))

    def __repr__(self) -> str:
        return "{self.sno}, {self.title}"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        pass
    return render_template('login.html')

@app.route('/register')
def register(request):
    if request.method == 'POST':
        pass
    return render_template('register.html')
