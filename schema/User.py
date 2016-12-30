# schema/User.py
# User scheme
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
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
        user.create() 
        ok = True
        return CreateUser(user=user)


class CreateUserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(mutation=CreateUserMutation,
                        query=Query,
                        types=[User],
                        auto_camelcase=False)
