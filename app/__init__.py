from flask import Flask

# Creating of the Flask application object
flask_microblog = Flask(__name__)
flask_microblog.config.from_object('config')

from app import views