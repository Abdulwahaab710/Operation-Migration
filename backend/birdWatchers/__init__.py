from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# Create an Instance of Flask
app = Flask(__name__, static_url_path='/static')
# Include config from config.py
app.config.from_object('config')
app.secret_key = 'some_secret'
# Create an instance of SQLAclhemy
db = SQLAlchemy(app)
from birdWatchers import views, models
