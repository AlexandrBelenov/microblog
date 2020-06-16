from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

# Creating of the Flask application object
flask_microblog = Flask(__name__)
flask_microblog.config.from_object('config')
db = SQLAlchemy(flask_microblog)

lm = LoginManager()
lm.init_app(flask_microblog)
lm.login_view = 'login'
oid = OpenID(flask_microblog, os.path.join(basedir, 'tmp'))
from app import models, views
