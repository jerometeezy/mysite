class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://jtz05:'
        'jtz12345'
        '@jtz05.mysql.pythonanywhere-services.com/'
        'jtz05$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False