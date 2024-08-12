import pytest
from app import create_app, db
from app.models import User

@pytest.fixture(scope='module')
def test_client():
    # Configurar la aplicación para pruebas
    app = create_app('testing')
    testing_client = app.test_client()

    # Establecer el contexto de la aplicación
    ctx = app.app_context()
    ctx.push()

    # Crear las tablas de la base de datos
    db.create_all()

    yield testing_client  # Esto es donde las pruebas se ejecutan

    # Limpiar la base de datos y el contexto
    db.session.remove()
    db.drop_all()
    ctx.pop()

def test_index(test_client):
    # Usar el cliente de prueba para enviar una solicitud GET al índice
    response = test_client.get('/')
    assert response.status_code == 302
    assert '/login' in response.headers['Location']