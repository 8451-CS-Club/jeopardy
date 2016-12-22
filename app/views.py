from flask import render_template, request
from app import app


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_categories/', methods = ['POST'])
def get_categories():
	return "categories here"

@app.route('/get_questions_in_cat/', methods = ['POST'])
def get_questions_in_cat():
	return "questions_here"
