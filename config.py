import os


class Config:

    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABSE_URL")
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/pitch_test'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}