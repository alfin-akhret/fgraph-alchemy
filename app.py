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
# Database initiation
# -----------------------------------------------------
from models import db
db.init_app(app)
db.create_all(app=app)

# ----------------------------------------------------
# GraphQL configuration
# ----------------------------------------------------
from flask_graphql import GraphQLView
from schema.User import schema, User
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

# ----------------------------------------------------
# Run the flask server
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )
