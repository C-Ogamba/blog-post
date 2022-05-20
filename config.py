import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLACHEMY_TRACK_MODIFICATIONS = False
