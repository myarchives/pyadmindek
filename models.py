import config
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(config.MYSQL_CONNECTION_URL, encoding="utf-8")

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(256), nullable=False)
    password=Column(String(256), nullable = False)
