import random,json,requests
from flask import render_template,flash,request,redirect,session,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.wrappers import response
from rentalapp import rent,form,db,mail,Message
from rentalapp.models import Property, Student,Post

@rent.route('/')
def home():
    return render_template('user/home.html')

@rent.route('/register',methods=['GET','POST'])
def register():
    up=form.Signup()
    if request.method =='GET':
     return render_template('user/register.html',up=up)  
    else:
        fname=request.form.get('firstname')  
        lname=request.form.get('lastname')
        number=request.form.get('number')
        email=request.form.get('mail')
        password=request.form.get('password')
        state=request.form.get('state')
        matric=request.form.get('matric')
        passw=generate_password_hash(password)
        g=Student(student_name=fname + lname,student_phone=number,student_email=email,student_state=state,student_matric=matric,student_col=passw)
        db.session.add(g)
        db.session.commit()
        Message()
        msg=Message(subject='Registered successfully',sender='ayokunleopadayo@gmail.com',
        recipients=[email],body='Successfully registered mail')
        mail.send(msg)
    return  redirect(url_for('home'))


@rent.route('/login',methods=['POST','GET'])
def login():
    if request.method =='GET':
        return render_template('user/login.html')
    else:
        user=request.form.get('name')
        word=request.form.get('word')
        record=db.session.query(Student).filter(Student.student_email==user).first()
        if record:
            loggedin_user =record.id
            hashedpass =record.student_col
            check=check_password_hash(hashedpass,word)
            flash(check)
            if check:
                session['user']=loggedin_user
                return redirect (url_for('dash'))
             
            else:
                flash('Invalid credentials') 
                return redirect(url_for('dash'))
        else:
            
         flash('Invalid Credientials,please try to login again')
         return   redirect('/dash')

@rent.route('/dash',methods=['POST','GET'])    
def dash():
    loggedin_user=session.get('user')
    if loggedin_user:
        response=requests.get('http://127.0.0.1:8082/hostel/api/v1.0/listall')
        dat=json.loads(response.text)
        return render_template('user/dashboard.html',dat=dat)
    else:
        return redirect ('/login')    
  





























