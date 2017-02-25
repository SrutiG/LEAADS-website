from app import app
from flask import render_template, request, url_for, redirect, flash, session

@app.route('/')
def index():
    session['login'] = True
    return redirect('home')

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
    login = session.get('login')
    user = "Example User"
    return render_template('home.html', login=login, user=user)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/opportunities_list')
def opportunities_list():
    return render_template('opportunities_list.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')


