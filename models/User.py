# models/user.py
# The user model
from sqlalchemy import Column, Integer, String, DateTime
from app import Base

class User(Base):
    __tablename__   = 'user'
    id              = Column(Integer, primary_key=True)
    username        = Column(String(140))
    password        = Column(String(140)) 
