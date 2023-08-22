from flask import Flask,render_template,request,redirect,session,Response
from flask_mysqldb import MySQL
import MySQLdb.cursors

app=Flask(__name__)
app.secret_key='qwer' 

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "project"

mysql = MySQL(app)
n=''
@app.route("/")
def create():
    return render_template('home.html')

@app.route('/signup.html',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        reg=request.form
        name=reg['name']
        email=reg['email']
        password=reg['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO signup(name,email,password) VALUES(%s, %s, %s)",(name, email, password))
        mysql.connection.commit()
        cur.close()
        return redirect('login.html')
    return render_template('signup.html')

@app.route('/',methods=['GET','POST'])
@app.route('/login.html',methods=['GET','POST'])
def login():
    s=''
    if request.method=='POST' and 'email' in request.form and 'password' in request.form:
        email=request.form['email']
        password=request.form['password']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)    
        cur.execute("select * from signup where email=%s and password=%s",(email,password,))
        user = cur.fetchone()
        if user:
            session['loggedin']=True
            session['name']=user['name']
            session['email']=user['email']
            session['password']=user['password']
            n=user['name']
            return render_template('home1.html')
        else:
            s='Please enter valid email/password!'       
    return render_template('login.html',s=s)

@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('name',None)
    session.pop('email',None)
    session.pop('password',None)
    return redirect('login.html')

@app.route('/home1.html')
def logo():
    return render_template('home1.html')

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/mainprofile.html')
def mainprofile():
    return render_template('mainprofile.html')

@app.route('/mainprofile2.html')
def mainprofile2():
    return render_template('mainprofile2.html')

@app.route('/mainprofile3.html')
def mainprofile3():
    return render_template('mainprofile3.html')

@app.route('/mainprofile4.html')
def mainprofile4():
    return render_template('mainprofile4.html')

@app.route('/mainprofile5.html')
def mainprofile5():
    return render_template('mainprofile5.html')

@app.route('/mainprofile6.html')
def mainprofile6():
    return render_template('mainprofile6.html')

@app.route('/profile.html')
def mentor():
    return render_template('profile.html')

@app.route('/profile1.html/<string:n>')
def profile(n):
    cur = mysql.connection.cursor()
    cur.execute("SELECT name,email FROM signup WHERE name = %s", (n,))
    data = cur.fetchone() 
    cur.close()
    return render_template('profile1.html', data=data)

@app.route('/profile.html',methods=['GET','POST'])
def mentor_profile():
    if request.method == 'POST':
        reg=request.form
        name=reg['name']
        email=reg['email']
        designation = reg['designation']
        work_location=reg['work_location']
        education=reg['education']
        description=reg['description']
        youtube_link=reg['youtube_link']
        linkedin_link=reg['linkedin_link']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mentor(name,email,designation,work_location,education,description,youtube_link,linkedin_link) VALUES(%s, %s, %s,%s, %s ,%s, %s,%s)",(name,email,designation,work_location,education,description,youtube_link,linkedin_link))
        mysql.connection.commit()
        cur.close()
        return redirect('home1.html')
    return render_template('profile.html')



if __name__=="__main__":
    app.run(debug=True)