from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit  # Importación corregida
from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))
    from app.forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        from app.models import User
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main_bp.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':  # Uso de urlsplit
            next_page = url_for('main_bp.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@main_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.index'))

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))
    from app.forms import RegistrationForm
    form = RegistrationForm()
    if form.validate_on_submit():
        from app.models import User
        from app import db
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_bp.login'))
    return render_template('register.html', title='Register', form=form)
