from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    name= StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    surname= StringField('Surname', validators=[DataRequired(), Length(min=2, max=20)])
    email= StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Sign')


class LoginForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password= PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Sign')