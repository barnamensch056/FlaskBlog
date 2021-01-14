from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,EqualTo,Length


class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])

    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit =  SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(),EqualTo('username')])

    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit= SubmitField('Log In')
