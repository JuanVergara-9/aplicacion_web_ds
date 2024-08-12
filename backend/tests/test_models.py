from app import create_app, db
from app.models import User, Product, Order, OrderItem, Expense
import unittest

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        # Configura la aplicación en modo de prueba
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Crea todas las tablas en la base de datos de prueba
        db.create_all()

    def tearDown(self):
        # Elimina la sesión de la base de datos y las tablas
        db.session.remove()
        db.drop_all()
        # Cierra el contexto de la aplicación
        self.app_context.pop()

    def test_model_insertions(self):
        # Crear y agregar un usuario de prueba
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('password123')
        db.session.add(user)

        # Crear y agregar un producto de prueba
        product = Product(name='Test Product', price=10.99, stock=100)
        db.session.add(product)

        # Crear y agregar un gasto de prueba
        expense = Expense(description='Test Expense', amount=50.0)
        db.session.add(expense)

        # Crear y agregar un pedido de prueba
        order = Order(table_number=1, status='pending')
        db.session.add(order)
        db.session.commit()  # Commit para que order tenga un id

        # Crear y agregar un ítem de pedido de prueba
        order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=2)
        db.session.add(order_item)

        # Confirmar cambios
        db.session.commit()

        # Verificar que las inserciones se realizaron correctamente
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(Product.query.count(), 1)
        self.assertEqual(Expense.query.count(), 1)
        self.assertEqual(Order.query.count(), 1)
        self.assertEqual(OrderItem.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
