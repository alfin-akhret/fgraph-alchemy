from flask import Flask
import sys

# -----------------------------------------------------
# App Configuration
# -----------------------------------------------------
app = Flask(__name__)
app.config.from_object('config')
# dont write .pyc files
sys.dont_write_bytecode = True

# ----------------------------------------------------
# Run the flask server
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
