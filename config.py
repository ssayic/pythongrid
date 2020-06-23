import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    ABS_PATH = '/'

    
    # mysql 
    PYTHONGRID_DB_HOSTNAME = ''
    PYTHONGRID_DB_NAME = 'sys'
    PYTHONGRID_DB_USERNAME = 'root'
    PYTHONGRID_DB_PASSWORD = 'Selim.1083'
    PYTHONGRID_DB_TYPE = 'mysql+pymysql'
    PYTHONGRID_DB_SOCKET = '/Applications/MAMP/tmp/mysql/mysql.sock'
    PYTHONGRID_DB_CHARSET = 'utf-8'
