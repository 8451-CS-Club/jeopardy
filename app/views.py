from flask import render_template, request, jsonify
from app import app


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/get_categories/', methods = ['POST'])
def get_categories():
	try:
		n_cat = request.form['n_cat']
	except:
		return "ERROR: Bad get_categories request"
	#This needs to be implemented:
	#return $DAVIS_API_get_categories(n_cat)
	return "categories_here"

@app.route('/get_questions_in_cat/', methods = ['POST'])
def get_questions_in_cat():
	try:
		category = request.form['category']
		n_q = request.form['n_q']
	except:
		return "ERROR: Bad get_questions_in_cat request"
	#This needs to be implemented:
	#data = $DAVIS_API_get_questions_in_cat(category, n_q)
	#TEMPORARY - Fake data returned
	data = {'q':'a', 'question':'answer'}
	return jsonify(**data)
