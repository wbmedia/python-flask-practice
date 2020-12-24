from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User


def codi_validator(form, field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('Username Codi is not allowed')


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError("You Need to be a human to register! ")


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
        validators.length(min=5, max=50, message='Username Field is Required'),
        codi_validator
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

    honeypot = HiddenField("", [length_honeypot])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError("Username Already in Use!")

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError("Email Already in Use!")

    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password.data) < 6:
            self.password.errors.append("Password need to be min 6 characters of length")
            return False

        return True


class TaskForm(Form):
    title = StringField('Title', [
        validators.length(min=4, max=60, message="Title out of range."),
        validators.DataRequired(message="Title is required.")

    ])

    description = TextAreaField('Description', [
        validators.DataRequired(message='Description is required.')
    ], render_kw={'rows': 5})
