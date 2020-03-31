import sys
from models import *
import hashlib
import hmac
import base64

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print(">> init db tables..")
    init_db()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create-admin':
            admin_password_1 = input("Please input admin password: ")
            while len(admin_password_1) <= 4:
                print("Password too short!")
                admin_password_1 = input("Please input admin password: ")
            admin_password_2 = input("Please input admin password again: ")
            if admin_password_1 != admin_password_2:
                print("Password not match!")
            else:
                new_password = base64.b64encode(
                    hmac.new(config.PASSWORD_SECRET.encode('utf-8'), admin_password_1.encode('utf-8'), digestmod=hashlib.sha256).digest())
                admin = session.query(User).filter(User.username == 'admin').first()
                if admin:
                    admin.password = new_password
                    session.commit()
                else:
                    admin = User(username='admin', password=new_password)
                    session.add(admin)
                    session.commit()
                print('OK')
