from datetime import datetime
from flask import Flask,render_template,url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Th1s154R4nD0mk3Y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db =SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    userName = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpeg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)      #one to many relationship here

    def __repr__(self):
        return f"User('{self.userName}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr(self):
        return f"Post('{self.title}','self.date_posted')"

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


if __name__=='__main__':
    app.run(debug=True)
