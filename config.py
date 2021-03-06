import os


# Default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '.\x12\xbc\xc04\xc76\xd0d\xa7NF\xb9\xe9uJ\xa4\x017\xed(\x07\xd7D'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	#print SQLALCHEMY_DATABASE_URI


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):  # Test commit
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False
