from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=5, max=50, message='Username is Required')
    ])
    password = PasswordField('Password', [
        validators.Required(message='Password is Required'),
        validators.length(min=6, max=50)
    ])


class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=5, max=50, message='Username Field is Required')
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.Required(message='Email Field is Required.'),
        validators.Email(message='Email needs to be valid.')
    ])

    password = PasswordField('Password', [
        validators.Required(message='Password Is Required'),
        validators.EqualTo('confirm_password', message='Password Not Match')
    ])
    confirm_password = PasswordField('Confirm Password')

    accept = BooleanField([
        validators.DataRequired()
    ])