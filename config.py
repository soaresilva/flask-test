import os

# environment variables
TESTING = os.environ.get('TESTING')
DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')

# MySQL config
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'USERNAME'
MYSQL_PASSWORD = 'PASSWORD'
MYSQL_DATABASE_DB = 'event_registration'
