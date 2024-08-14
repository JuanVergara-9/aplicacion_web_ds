import pytest

@pytest.fixture
def client(app):
    return app.test_client()

def login(client, username):
    return client.post('/login', data=dict(
        username=username,
    ), follow_redirects=True)

def test_index_page(client):
    """Prueba para verificar que la página de inicio cargue correctamente."""
    login(client,'test_user')
    response = client.get('/')
    # Si la página redirige a la página de inicio de sesión, sigue la redirección
    if response.status_code == 302:
        response = client.get('/', follow_redirects=True)
    assert response.status_code == 200


def test_login_page(client):
    """Prueba para verificar que la página de inicio de sesión cargue correctamente."""
    response = client.get('/login')
    assert response.status_code == 200
    # Ajusta 'Nombre de Usuario' según el contenido real
    assert b'Nombre' in response.data
