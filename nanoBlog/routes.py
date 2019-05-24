from flask import render_template,url_for,flash, redirect,request
from nanoBlog import app,db,bcrypt
from nanoBlog.forms import RegistrationForm,LoginForm
from nanoBlog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(userName=form.userName.data,email=form.email.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created','success')

        return redirect(url_for('login')) #function home
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login Successful','danger')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful','danger')
    return render_template('login.html',title='Login',form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title='Account')
