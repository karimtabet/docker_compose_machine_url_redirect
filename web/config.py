import os


class BaseConfig(object):
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    SECRET_KEY = os.environ['SECRET_KEY']
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TWITTER_CONSUMER_KEY = 'bxoaJl4m7TsaBxBpo7oVywp2h'
    TWITTER_CONSUMER_SECRET = (
        'uOJaZhdT7fE8VhMNq8ZPafdMP4nbnN2ydc6P9USUX0PPLeMsO1'
    )
