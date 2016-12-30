# schema/User.py
# User scheme
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db
from models.User import User as UserModel

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)
    user  = graphene.Field(User, id=graphene.Int())

    def resolve_users(self, args, context, info):
        query = User.get_query(context) # SQLAlchemy query
        return query.all()

    def resolve_user(self, args, context, info):
        query = User.get_query(context)
        return query.filter(UserModel.id==args['id']).first()
    
# Mutation
class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String()
        password = graphene.String()
    
    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)
    
    def mutate(self, args, context, info):
        user = UserModel(username=args.get('username'),
                        password=args.get('password'))
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


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(mutation=UserMutation,
                        query=Query,
                        types=[User],
                        auto_camelcase=False)
