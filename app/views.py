from flask import render_template, request
from app import app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/game')
def game():
    return render_template('game.html')
