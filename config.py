import os

TESTING = os.environ.get('TESTING')
DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')

# MySQL config
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_UNIX_SOCKET = '/Applications/mampstack-7.3.13-0/mysql/tmp/mysql.sock'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'rootrootroot'
MYSQL_DB = 'flask_event_reg'
MYSQL_CURSORCLASS = 'DictCursor'