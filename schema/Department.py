# schema/Department.py
# Department schema
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db
from models.User import Department as DepartmentModel

class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel

class Query(graphene.ObjectType):
    departments = graphene.List(Department)
    department  = graphene.Field(Department, id=graphene.Int())

    def resolve_departments(self, args, context, info):
        query = Department.get_query(context)
        return query.all()

    def resolve_department(self, args, context, info):
        query = User.get_query(context)
        return query.filter(DepartmentModel.id==args['id']).firts()

#Mutation
class CreateDepartment(graphene.Mutation):
    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    department = graphene.Field(lambda: Department)

    def mutate(self, args, context, info):
        department = DepartmentModel(name=args.get('name'))
        db.session.add(department)
        db.session.commit()
        ok = True
        return CreateDepartment(department=department, ok=ok)

class DeleteDepartment(graphene.Mutation):
    class Input:
        id = graphene.Int()

    ok = graphene
    department = graphene.Field(lambda: Department)
    
    def mutate(self, args, context, info):
        department = db.session.query(DepartmentModel).filter_by(id=args.get('id')).firts()
        db.session.delete(department)
        db.session.commit()
        ok = True
        return DeleteDepartment(department=department, ok=ok)

class DepartmentMutation(graphene.ObjectType):
    create_department = CreateDepartment.Field()
    delete_department = DeleteDepartment.Field()

schema = graphene.Schema(mutation=DepartmentMutation,
                        query=Query,
                        types=[Department],
                        auto_camelcase=False)
        
