from flask import Flask

# Creating of the Flask application object
flask_microblog = Flask(__name__)

from app import views
