from app import app
from flask import render_template, request, url_for, redirect, flash, session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    login = True
    user = "Firstname Lastname"
    return render_template('home.html', login=login, user=user)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/opportunities_list')
def opportunities_list():
    return render_template('opportunities_list.html')
