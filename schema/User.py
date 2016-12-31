# schema/User.py
# User scheme
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db
from models.User import User as UserModel

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

    
# Mutation
class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String()
        password = graphene.String()
        department_id = graphene.Int()
    
    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)
    
    def mutate(self, args, context, info):
        user = UserModel(username=args.get('username'),
                        password=args.get('password'),
                        department_id=args.get('department'))
        db.session.add(user)
        db.session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)

class DeleteUser(graphene.Mutation):
    class Input:
        id = graphene.Int()

    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)

    def mutate(self, args, context, info):
        user = db.session.query(UserModel).filter_by(id=args.get('id')).first()
        db.session.delete(user)
        db.session.commit()
        
        ok = True 
        return DeleteUser(user=user, ok=ok)
