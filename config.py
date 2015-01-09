import os


# Default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '.\x12\xbc\xc04\xc76\xd0d\xa7NF\xb9\xe9uJ\xa4\x017\xed(\x07\xd7D'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False
