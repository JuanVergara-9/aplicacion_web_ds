import pytest
from app import create_app, db
from app.models import User  # Ajusta esto según tu modelo

@pytest.fixture
def app():
    app = create_app('testing')  # Asegúrate de tener un config para testing
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()  # Crea las tablas

    yield app

    with app.app_context():
        db.drop_all()  # Elimina las tablas al finalizar
