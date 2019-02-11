import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/pitch'