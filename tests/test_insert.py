from app import create_app, db
from app.models import User, Product, Order, OrderItem, Expense
import unittest

class InsertTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_insert_data(self):
        # Crear un usuario de prueba
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('password123')
        db.session.add(user)

        # Crear un producto de prueba
        product = Product(name='Test Product', price=10.99, stock=100)
        db.session.add(product)

        # Crear un gasto de prueba
        expense = Expense(description='Test Expense', amount=50.0)
        db.session.add(expense)

        # Crear un pedido de prueba
        order = Order(table_number=1, status='pending')
        db.session.add(order)
        db.session.commit()  # Commit para que order tenga un id

        # Crear un ítem de pedido de prueba
        order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=2)
        db.session.add(order_item)

        # Confirmar cambios
        db.session.commit()

        # Verificar inserciones
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(Product.query.count(), 1)
        self.assertEqual(Expense.query.count(), 1)
        self.assertEqual(Order.query.count(), 1)
        self.assertEqual(OrderItem.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
