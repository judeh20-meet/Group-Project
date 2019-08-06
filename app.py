from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')
def go_donate():
    return render_template("donate.html")

@app.route('/donate')
def donate():
    return render_template('donate.html')

if __name__ == '__main__':
    app.run(debug=True)