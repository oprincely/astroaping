from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
#
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/')
def hello():
    return "Hello World!"