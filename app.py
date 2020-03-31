from flask import *
from models import *
import json
import time
import auth

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)

def to_json(data):
    return json.dumps(data, cls=DatetimeEncoder)


def logined():
    return 'username' in session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# ----------------------------- Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.values.get("username")
        password = request.values.get("password")
        user = db.query(User).filter(User.username == username).first()
        if user and user.password.encode('utf-8') == auth.enc(password):
            session['username'] = username
            return to_json({'code': '200','message': 'OK'})
        else:
            return to_json({'code': '500', 'message': 'Wrong Username/Password'})
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if logined():
        return render_template("dashboard.html")
    else:
        return redirect('login')
