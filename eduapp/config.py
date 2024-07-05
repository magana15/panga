import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'magana'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///eduwear.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
