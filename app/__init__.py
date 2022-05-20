from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_bcrypt import Bcrypt
import logging
from logging.handlers import RotatingFileHandler
import os


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)
bcrypt = Bcrypt(app)

from app import routes, models
