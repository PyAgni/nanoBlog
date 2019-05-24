from flask import render_template,url_for,flash, redirect
from nanoBlog import app
from nanoBlog.forms import RegistrationForm,LoginForm
from nanoBlog.models import User,Post
from nanoBlog import db

posts = [
    {
        'author': 'Agni',
        'title': 'Python blog',
        'content': 'Scripting in python',
        'date_posted': 'May 23, 2019'
    },
    {
        'author': 'Agni',
        'title': 'Python blog',
        'content': 'Scripting in python',
        'date_posted': 'May 23, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accounted created for {form.userName.data}!','success')
        # new_username = form.userName.data
        # new_email = form.email.data
        # new_password = form.password.data
        #
        # form_data = User(userName=new_username,email=new_email,password=new_password)
        # db.session.add(form_data)
        # db.session.commit()

        return redirect(url_for('home')) #function home
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'agni@gmail.com' and form.password.data == 'password':
            flash('Yayy! Youre logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful','danger')
    return render_template('login.html',title='Login',form=form)
