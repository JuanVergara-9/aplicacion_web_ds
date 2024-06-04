from app import create_app, db
from flask_migrate import MigrateCommand
from flask_script import Manager # type: ignore

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)
