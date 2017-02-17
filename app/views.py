from app import app
from flask import render_template, request, url_for, redirect, flash, session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/profileform')
def profileform():
    return render_template('profileform.html')


@app.route('/opportunitydetail')
def opportunitydetail():
    return render_template('opportunitydetail.html')


@app.route('/home')
def home():
     return render_template('home.html')
