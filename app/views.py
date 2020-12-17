from flask import Blueprint
from flask import render_template, request

from .models import User
from .forms import LoginForm, RegisterForm

page = Blueprint('page', __name__)


@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title="404"), 404


@page.route('/')
def index():
    return render_template('index.html', title="Index")


@page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form.username.data)
        print(form.password.data)

    return render_template('auth/login.html', title="Login", form=form)


@page.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            print("User Created Success!")

    return render_template('auth/register.html', title="Register", form=form)
