from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField,DecimalField
from wtforms.validators import ValidationError,DataRequired,Email,EqualTo,Length
from flask_wtf.file import FileField,FileRequired,FileAllowed
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('EmailId',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()]) 
    email = StringField('EmailId',validators=[DataRequired()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    repassword = PasswordField('Retype Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address already in use.')

class AddProductForm(FlaskForm):
    name = StringField('Title',validators=[DataRequired()])
    category = StringField('Category',validators=[DataRequired()])
    price = DecimalField('Price',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired(),Length(min=1,max=140)])
    image = FileField('Image',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'],'Images only!')])
    quantity = StringField('Quantity',validators=[DataRequired()])
    submit = SubmitField('Submit')

