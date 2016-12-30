# schema/User.py
# User scheme
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app import db_session
from models import User as UserModel

schema = graphene.Schema()

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel.User
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()

schema.query = Query
