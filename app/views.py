from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/checkin')
def check_in():
	form = LoginForm()
	return render_template("index.html", form=form)