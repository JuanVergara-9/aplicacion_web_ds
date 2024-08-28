from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask import Blueprint
from .extension import db

main_bp = Blueprint('main_bp', __name__)

# Rutas para la página de inicio y login
@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home', username=current_user.username, codigo_mesa=current_user.codigo_mesa)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        codigo_mesa = request.form['codigo_mesa']

        # Buscar si el usuario ya existe
        user = User.query.filter_by(username=username).first()

        if user is None:
            # Crear un nuevo usuario si no existe
            new_user = User(username=username, codigo_mesa=codigo_mesa)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash(f'Usuario {username} registrado y logueado exitosamente')
            return redirect(url_for('main_bp.index'))

        # Si el usuario ya existe, simplemente loguearlo
        if user.codigo_mesa == codigo_mesa:
            login_user(user)
            flash(f'Bienvenido de nuevo, {username}!')
            return redirect(url_for('main_bp.index'))
        else:
            flash('Código de mesa incorrecto.')

    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.index'))

# Nueva ruta para el menú
@main_bp.route('/menu')
@login_required
def menu():
    return render_template('menu.html', title='Menú')
