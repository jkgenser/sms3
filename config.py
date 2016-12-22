import os

class DefaultConfig(object):
    SECRET_KEY = 'secret_key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    TWILIO_NUMBER = os.environ['TWILIO_NUMBER']


class DevelopmentConfig(DefaultConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]