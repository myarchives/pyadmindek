import hashlib
import hmac
import base64
import config

def enc(password):
    return base64.b64encode(
        hmac.new(config.PASSWORD_SECRET.encode('utf-8'), password.encode('utf-8'), digestmod=hashlib.sha256).digest())
