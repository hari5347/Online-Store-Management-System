from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError,DataRequired,Email,EqualTo,Length
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('EmailId',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()]) 
    email = StringField('EmailId',validators=[DataRequired()])
    username = StringField('Username',validators=[DataRequired()])
    country = StringField('country')
    password = PasswordField('Password',validators=[DataRequired()])
    repassword = PasswordField('Retype Password',validators=[DataRequired(),EqualTo('password')])
    address = StringField('Address')
    submit = SubmitField('Register')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address already in use.')
