# models/Department.py
# The department model
from sqlalchemy import Column, Integer, String
from models import db

class Department(db.Model):
    __tablename__   = 'departments'
    id              = Column(Integer, primary_key=True)
    name            = Column(String(140)) 
