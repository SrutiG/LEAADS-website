from app import app, mysql
from flask import render_template, request, url_for, redirect, flash, session
from werkzeug.utils import secure_filename
import os
import json
import time 


@app.route('/')
def index():
    return redirect('home')



@app.route('/profile')
def profile():
    user = session.get('user')
    session['login'] = True
    login = session['login']
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE USERNAME = '" + user + "';") # * b/c all info
    userInfo = cursor.fetchall()
    cursor.execute("SELECT * FROM USER_OPP WHERE USERNAME = '" + user + "';")
    opps = cursor.fetchall()
    return render_template('profile.html', userInfo = userInfo, opps=opps, login=login, user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER WHERE USERNAME = %s AND PASSWORD =%s",(username, password))
        loginstr = cursor.fetchall()
        if len(loginstr) > 0: 
            session['login'] = True
            session['user'] = username
            return json.dumps({'success':True}), 200
        return json.dumps({'error': True}), 400

@app.route('/profileform')
def profileform():
    return render_template('profileform.html')

@app.route('/logout')
def logout():
    session['login'] = False
    session['user'] = None
    return redirect('home')

@app.route('/opportunitydetail')
def opportunitydetail():
    return render_template('opportunitydetail.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        email = request.form['email']
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
        descript = request.form['descript']
        courtStr = request.form['court']
        parentName = request.form['parentName']
        if courtStr == "0":
            court = 0
        else:
            court = 1
        number = request.form['number']
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USER (USERNAME,PASSWORD,EMAIL,NAME, AGE, DESCRIPT, ADDRESS, COURT,GENDER,NUMBER, PARENTNAME) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (username, password, email, name, age, descript, address, court, gender, number, parentName))
        conn.commit()
        session['login'] = True
        session['user'] = username
        return json.dumps({'success':True}), 200


@app.route('/home')
def home():
    login = session.get('login')
    user = session.get('user')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PHOTO;")
    photos = cursor.fetchall()
    cursor.execute("SELECT * FROM OPPORTUNITY INNER JOIN OPP_TIME ON OPPORTUNITY.NAME = OPP_TIME.NAME WHERE CATEGORY = 'Event' ORDER BY OPP_TIME.DATE ASC;")
    events = cursor.fetchall()
    return render_template('home.html', login=login, user=user, photos=photos, events = events)

@app.route('/about_us')
def about_us():
    login = session.get('login')
    user = session.get('user')
    return render_template('about_us.html', login=login, user=user)

@app.route('/overtheyears')
def overtheyears():
    login = session.get('login')
    user = session.get('user')
    return render_template('overtheyears.html', login=login, user=user)

@app.route('/opportunities_list', methods=["GET", "POST"])
def opportunities_list():
    login = session.get('login')
    user = session.get('user')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OPPORTUNITY")
    opportunities = cursor.fetchall()
    return render_template('opportunities_list.html', opportunities = opportunities, login=login, user=user)

@app.route('/opportunities_list_category/<category>', methods = ["GET"])
def opportunities_list_category(category):
    login = session.get('login')
    user = session.get('user')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OPPORTUNITY WHERE CATEGORY = '" + category + "';")
    opportunities = cursor.fetchall()
    return render_template('opportunities_list.html', opportunities = opportunities, login=login, user=user)

@app.route('/blog')
def blog():
    login = session.get('login')
    user = session.get('user')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NEWS ORDER BY DATE DESC;")
    blogPosts = cursor.fetchall()
    return render_template('blog.html', blogPosts=blogPosts, login=login, user=user)

@app.route('/programs')
def programs():
    login = session.get('login')
    user = session.get('user')
    return render_template('programs.html', login=login, user=user)

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

@app.route('/getImage', methods=['GET', 'POST'])
def getImage():
    photo = request.files['croppedImage']
    filename = secure_filename(request.form['filename'])
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/admin_home', methods=['GET', 'POST'])
def admin_home():
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    if request.method == 'POST':
        photo = request.files['photo']
        caption = request.form['caption']
        filename = secure_filename(photo.filename)
        cursor.execute("INSERT INTO PHOTO VALUES(%s, %s)", (filename, caption,))
        conn.commit()
        return redirect('admin_home')

    cursor.execute("SELECT * FROM PHOTO;")
    photos = cursor.fetchall()
    user = session.get('admin')
    return render_template('admin-home.html', user = user, photos=photos)

@app.route('/admin_blog', methods=['GET', 'POST'])
def admin_blog():
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    user = session.get('admin')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("SELECT NAME FROM ADMIN WHERE USERNAME = '" + user +  "';")
        adminVals = cursor.fetchall()
        admin = adminVals[0][0]
        title.replace("'", "''")
        cursor.execute("INSERT INTO NEWS VALUES(CURDATE(), %s, 'None', %s, %s);", (admin, content, title,))
        conn.commit()
        return redirect('admin_blog')

    cursor.execute("SELECT * FROM NEWS ORDER BY DATE DESC;");
    posts = cursor.fetchall()

    return render_template('admin-blog.html', user = user, posts = posts)

@app.route('/admin_prog')
def admin_prog():
    if not session.get('admin_login'):
        return redirect('admin')
    user = session.get('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT USERNAME FROM USER_PROG WHERE PROG_NAME = 'Learning Center';")
    lc = cursor.fetchall()
    cursor.execute("SELECT USERNAME FROM USER_PROG WHERE PROG_NAME = 'Summer Camp';")
    sc = cursor.fetchall()
    cursor.execute("SELECT USERNAME FROM USER_PROG WHERE PROG_NAME = 'Foundations Youth Leadership and Mentoring Program';")
    fp = cursor.fetchall()
    return render_template('admin-prog.html', user = user, lc=lc, sc=sc, fp=fp)

@app.route('/admin_opp', methods=['GET', 'POST'])
def admin_opp():
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    user = session.get('admin')
    cursor.execute("SELECT NAME FROM OPPORTUNITY;")
    opps = cursor.fetchall()
    opp_members = {}
    for item in opps:
        cursor.execute("SELECT * FROM USER_OPP WHERE OPP_NAME = '" + item[0] + "'")
        opp_members[item[0]] = cursor.fetchall()

    if request.method == 'POST':
        oppname = request.form['oppname']
        date = request.form['date']
        timecom = request.form['timecom']
        location = request.form['location']
        category = request.form['category']
        description = request.form['description']

        cursor.execute("INSERT INTO OPPORTUNITY VALUES(%s, %s, %s, %s, %s, %s, 'none');", (oppname, date, timecom, location, category, description))
        conn.commit()
        return redirect('admin_opp')

    return render_template('admin-opp.html', opp_members = opp_members)

@app.route('/admin_members')
def admin_members():
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER;")
    members = cursor.fetchall()
    user = session.get('admin')
    return render_template('admin-members.html', user = user, members = members)

@app.route('/deletePost/<postName>/', methods = ['GET', 'POST'])
def deletePost(postName):
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    postName.replace("'", "''")
    cursor.execute("DELETE FROM NEWS WHERE TITLE = '" + postName + "';")
    conn.commit()
    return redirect('admin_blog')

@app.route('/deletePhoto/<photoName>/', methods = ['GET', 'POST'])
def deletePhoto(photoName):
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PHOTO WHERE PHOTO = '" + photoName + "';")
    conn.commit()
    return redirect('admin_home')

@app.route('/deleteMember/<member>/', methods = ['GET', 'POST'])
def deleteMember(member):
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USER WHERE USERNAME = '" + member + "';")
    conn.commit()
    return redirect('admin_members')

@app.route('/deleteOpp/<oppName>/', methods = ['GET', 'POST'])
def deleteOpp(oppName):
    if not session.get('admin_login'):
        return redirect('admin')
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM OPPORTUNITY WHERE NAME = '" + oppName + "';")
    conn.commit()
    return redirect('admin_opp')