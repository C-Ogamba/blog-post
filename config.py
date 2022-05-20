import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
