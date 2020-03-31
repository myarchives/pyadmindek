from models import *
import json
import time
from flask import *

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)

def to_json(data):
    return json.dumps(data, cls=DatetimeEncoder)

def auth():
    return 'username' in session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# ----------------------------- Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    session['username'] = 'Admin'
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if auth():
        return render_template("dashboard.html")
    else:
        return redirect('login')
