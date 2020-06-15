from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating of the Flask application object
flask_microblog = Flask(__name__)
flask_microblog.config.from_object('config')
db = SQLAlchemy(flask_microblog)


from app import views, models