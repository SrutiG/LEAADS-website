from app import app, mysql
from flask import render_template, request, url_for, redirect, flash, session


@app.route('/')
def index():
    session['login'] = True
    return redirect('home')

@app.route('/profile')
def profile():
    #user = session.get('user')
    user = "jhalpert"
    session['login'] = True
    login = session['login']
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE USERNAME = '" + user + "';") # * b/c all info
    userInfo = cursor.fetchall()
    cursor.execute("SELECT * FROM USER_OPP WHERE USERNAME = '" + user + "';")
    opps = cursor.fetchall()
    return render_template('profile.html', userInfo = userInfo, opps=opps, login=login, user=user)

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
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PHOTO;")
    photos = cursor.fetchall()
    return render_template('home.html', login=login, user=user)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/opportunities_list')
def opportunities_list():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OPPORTUNITY")
    opportunities = cursor.fetchall()
    return render_template('opportunities_list.html', opportunities = opportunities)

@app.route('/blog')
def blog():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NEWS;")
    blogPosts = cursor.fetchall()
    return render_template('blog.html', blogPosts=blogPosts)

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if not session.get('admin_login'):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ADMIN WHERE USERNAME = '" + username + "' AND PASSWORD = '" + password + "';")
            data = cursor.fetchall()
            if len(data) > 0:
                session['admin'] = username
                session['admin_login'] = True
                return redirect('admin_dashboard')
        return render_template('admin-login.html')
    else:
        return redirect('admin_dashboard')

@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('admin_login'):
        return redirect('admin')
    user = session.get('admin')
    return render_template('admin-dashboard.html', user = user)

@app.route('/admin_logout')
def admin_logout():
    session['admin'] = None
    session['admin_login'] = False
    return redirect('admin')


