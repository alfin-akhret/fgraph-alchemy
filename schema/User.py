# schema/User.py
# User scheme
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.User import User as UserModel

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )

class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String(name='username')
        password = graphene.String(name='password')
    
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

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(User)
    user = graphene.Field(User)
 
schema = graphene.Schema(mutation=CreateUserMutation,
                        query=Query,
                        types=[User],
                        auto_camelcase=False)
