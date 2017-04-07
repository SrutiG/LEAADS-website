from app import app, mysql
from flask import render_template, request, url_for, redirect, flash, session
import json


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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        # data = request.get_json()
        username = request.form['username'];
        password = request.form['password'];
        conn = mysql.connection;
        cursor = conn.cursor();
        cursor.execute("SELECT * FROM USER WHERE USERNAME = %s AND PASSWORD =%s",(username, password));
        loginstr = cursor.fetchall();
        if len(loginstr) > 0: 
            session['login'] = True;
            session['user'] = username; 
            return json.dumps({'success':True}), 200;
        return json.dumps({'error': True}), 400;



@app.route('/initsignup', methods = ['GET', 'POST'])
def initsignup():
    if (request.method == 'POST'):
        #data = request.get_json()
        username = request.form['username'];
        password = request.form['password'];
        confirmpassword = request.form['confirmpassword'];
        email = request.form['email'];
        conn = mysql.connection;
        cursor = conn.cursor();
        print confirmpassword;
       # cursor.execute("INSERT INTO USER VALUES(USERNAME = %s, PASSWORD = %s, EMAIL = %s", (username, password, email)));
        cursor.execute("INSERT INTO USER (USERNAME,PASSWORD,EMAIL) VALUES (%s,%s,%s)", (username,password,email));
        initstr = cursor.fetchall();
        if password == confirmpass: 
            session['login'] = True;
            session['user'] = username;
            return json.dumps({'success':True}), 200;

        return json.dumps({'error': True}), 400;

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if (request.method == 'POST'):
        #data = request.get_json()
        name = request.form['name'];
        age = request.form['age'];
        gender = request.form['gender'];
        address = request.form['address'];
        number = request.form['number'];
        descript = request.form['descript'];
        court = request.form['court'];

        conn = mysql.connection;
        cursor = conn.cursor();
        #cursor.execute("UPDATE USER WHERE USERNAME = username(NAME = %s, AGE = %s, DESCRIPT = %s, ADDRESS = %s, COURT = %s,GENDER = %s, NUMBER = %s",(name, age, descript, address,court, gender, number)));


        signupstr = cursor.fetchall();
        if len(signupstr) > 0: 
            session['login'] = True;
            session['user'] = username;
            return json.dumps({'success':True}), 200;

        return json.dumps({'error': True}), 400;


@app.route('/home')
def home():
    login = session.get('login')
    user = session.get('user')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PHOTO;")
    photos = cursor.fetchall()
    return render_template('home.html', login=login, user=user)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/overtheyears')
def overtheyears():
    return render_template('overtheyears.html')

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
                return redirect('admin_home')
        return render_template('admin-login.html')
    else:
        return redirect('admin_home')

@app.route('/admin_home')
def admin_home():
    if not session.get('admin_login'):
        return redirect('admin')
    user = session.get('admin')
    return render_template('admin-home.html', user = user)

@app.route('/admin_logout')
def admin_logout():
    session['admin'] = None
    session['admin_login'] = False
    return redirect('admin')


