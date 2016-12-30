from flask import Flask
import sys

# -----------------------------------------------------
# App Configuration
# -----------------------------------------------------
app = Flask(__name__)
app.config.from_object('config')
# dont write .pyc files
sys.dont_write_bytecode = True

# -----------------------------------------------------
# Database configuration
# -----------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(app.config['DATABASE_CONN'],
                    convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all models here
    from models.User import User
    
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# create db if not exist
init_db()

# ----------------------------------------------------
# GraphQL configuration
# ----------------------------------------------------
'''
from flask_graphql import GraphQLView
from schema import User
app.add_url_rule(
    'graphql',
    view_func=GraphQLView.as_view(
        schema=schema,
        graphiql=True
    )
)
'''

# ----------------------------------------------------
# Run the flask server
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )
