from sqlalchemy.exc import IntegrityError
import unittest
from app import create_app, db
from app.models import User

class TestUserModel(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la aplicación para las pruebas
        app = create_app('testing')
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        # Crear un nuevo usuario
        user = User(username='test_user', codigo_mesa=1)
        db.session.add(user)
        db.session.commit()

        # Verificar que el usuario se haya creado correctamente
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.codigo_mesa, 1)

    def test_user_unique_username(self):
        user1 = User(username='test_user', codigo_mesa=1)
        db.session.add(user1)
        db.session.commit()

        # Intentar crear un segundo usuario con el mismo nombre de usuario
        try:
            user2 = User(username='test_user', codigo_mesa=2)
            db.session.add(user2)
            db.session.commit()
            self.fail("IntegrityError expected but not raised")
        except IntegrityError:
            db.session.rollback()

            
        # Limpiar la base de datos después de cada prueba
        db.session.delete(user1)
        db.session.commit()
