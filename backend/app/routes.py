from flask import Flask, render_template
from flask import Blueprint

main = Blueprint('main',__name__)

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

