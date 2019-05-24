from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
    userName = StringField('Username',
                            validators=[DataRequired(),
                                        Length(min=3,max=10)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5)])
    confirm_password = PasswordField('Password',
                                    validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('SignUp')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
