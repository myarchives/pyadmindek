from models import *
import json
import time
import jinja2
from flask import *

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)

def to_json(data):
    return json.dumps(data, cls=DatetimeEncoder)

app = Flask(__name__)

# ----------------------------- Home
@app.route('/')
def home():
    return 'Hello, PyAdminDek!'
