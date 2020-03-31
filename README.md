# pyadmindek
A modern design admin dashboard system with admindek theme and python backend

## Deploy
```
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
sudo yum -y install mysql-server
sudo service mysqld restart
mysql -uroot
CREATE DATABASE pyadmindek CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'pyadmindek'@'localhost' IDENTIFIED BY 'PyAdminDek88';
GRANT ALL PRIVILEGES ON *.* TO 'pyadmindek'@'localhost';
FLUSH PRIVILEGES;
sudo yum -y install gcc openssl-devel bzip2-devel libffi-devel
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
tar xzf Python-3.8.0.tgz
cd Python-3.8.0
./configure --enable-optimizations
sudo make install
cd ..
sudo rm -rf Python-3.8.0*
sudo ln -s /usr/local/bin/python3.8 /usr/local/bin/python
sudo ln -s /usr/local/bin/pip3.8 /usr/local/bin/pip
sudo /usr/local/bin/pip install --upgrade pip
sudo /usr/local/bin/pip install gunicorn gevent flask jinja2 PyMySQL sqlalchemy 
git clone https://github.com/hide2/pyadmindek.git
cd pyadmindek
```

## Init Admin
```
python admin.py create-admin
```

## Start Server
```
FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0 --port=8888
or
./restart.sh
```

## Todo
* ~~Create User Model with SQLAlchemy ORM~~
* ~~python admin.py create-admin to init admin user~~
* ~~app.py models.py config.py~~
* login.html index.html
* login with user & password example
 