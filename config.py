import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:12345678@localhost/recipes_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

