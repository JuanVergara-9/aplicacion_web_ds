from flask_migrate import Migrate
from app import create_app

app = create_app()
migrate = Migrate(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
