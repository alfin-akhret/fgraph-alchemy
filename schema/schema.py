import graphene
from schema.Department import Department, CreateDepartment, DeleteDepartment
from schema.User import User, CreateUser, DeleteUser

class Query(graphene.ObjectType):
    # User Query
    users = graphene.List(User)
    user  = graphene.Field(User, id=graphene.Int())


    def resolve_users(self, args, context, info):
        query = User.get_query(context) # SQLAlchemy query
        return query.all()

    def resolve_user(self, args, context, info):
        query = User.get_query(context)
        return query.filter(UserModel.id==args['id']).first()

    # Department Query
    departments = graphene.List(Department)
    department  = graphene.Field(Department, id=graphene.Int())

    def resolve_departments(self, args, context, info):
        query = Department.get_query(context)
        return query.all()

    def resolve_department(self, args, context, info):
        query = User.get_query(context)
        return query.filter(DepartmentModel.id==args['id']).firts()



class Mutation(graphene.ObjectType):
    create_department = CreateDepartment.Field()
    delete_department = DeleteDepartment.Field()
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(mutation=Mutation,
                        query=Query,
                        types=[Department],
                        auto_camelcase=False)
 
