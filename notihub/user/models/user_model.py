from sqlalchemy import String, Column, Integer
from config.database.connect_db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String, unique=True, index=True)
    password = Column(String(25))

