# models/user.py
# The user model
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.Department import Department
from models import db

class User(db.Model):
    __tablename__   = 'users'
    id              = Column(Integer, primary_key=True)
    username        = Column(String(140))
    password        = Column(String(140)) 

    #relationship
    department_id   = Column(Integer, ForeignKey('departments.id'))
    department      = relationship('Department',
                                    backref=backref('users',
                                                    uselist=True,
                                                    cascade='delete,all'))

