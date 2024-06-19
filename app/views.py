from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from urllib.parse import urlsplit  # Importación corregida
from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)

valid_table_numbers = {1, 2, 3, 4, 5}

class User(UserMixin):
    def __init__(self, id, name, table_number):
        self.id = id
        self.name = name
        self.table_number = table_number

    @staticmethod
    def get(user_id):

        return User(user_id, "Placeholder", user_id)

@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home', name=current_user.name, table_number=current_user.table_number)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))
    if request.method == 'POST':
        name = request.form['name']
        table_number = int(request.form['table_number'])
        if table_number in valid_table_numbers:
            user = User(table_number, name, table_number)
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '': 
                next_page = url_for('main_bp.index')
            return redirect(next_page)
        else:
            flash('Número de mesa inválido')
            return redirect(url_for('main_bp.login'))
    return render_template('login.html', title='Ingreso Cliente')

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

@main_bp.route('/test_db')
def test_db():
    try:
        # Intentar una consulta simple
        users = User.query.all()
        return f'There are {len(users)} users in the database.'
    except Exception as e:
        return str(e)