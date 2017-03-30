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

@app.route(‘/login/, methods = [‘GET’, ‘POST’])
def login():
    if request.method == ‘POST’
        data = request.get_json()
        username = json_dict[‘username’]
        password = json_dict[‘password’]
        conn = mysql.connection 
        cursor = conn.cursor() 
        cursor.execute(“SELECT * FROM USER WHERE USERNAME = %s AND PASSWORD =%s”,(username, password)) 


        loginstr = cursor.fetchall()
        if len(loginstr) > 0: 
            session[‘login’] = True 
            session[‘user’] = username 
            return json.dumps({‘success':True}), 200

        return json.dumps({‘error’: True}), 400


@app.route(‘/signup/, methods = [‘GET’, ‘POST’])
def signup():
    if request.method == ‘POST’
        data = request.get_json()
        username = json_dict[‘username’]
        password = json_dict[‘password’]
        confirmpassword = json_dict['confirmpassword']
        email = json_dict['email']
        name = json_dict[‘name’]
        age = json_dict[‘age’]
        gender = json_dict['gender']
        address = json_dict['address']
        number = json_dict[‘number’]
        descript = json_dict[‘descript’]
        court = json_dict['court']

        conn = mysql.connection 
        cursor = conn.cursor() 
        cursor.execute(“SELECT * FROM USER WHERE USERNAME = %s, PASSWORD =%s, 
            NAME = %s, AGE = %i, DESCRIPT = %s, ADDRESS = %s, EMAIL =%s, COURT = %i,
            GENDER = %s, NUMBER = %i”,(username, password, name, age, descript, address,
                email, gender, number)) 


        signupstr = cursor.fetchall()
        if len(signupstr) > 0 && password == confirmpass: 
            session[‘login’] = True 
            session[‘user’] = username 
            return json.dumps({‘success':True}), 200

        return json.dumps({‘error’: True}), 400

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


