class DefaultConfig(object):

    DEBUG = False
    TESTING = False

    # image url
    # IMAGE_URL = 'http://image.sports.baofeng.com/'

    # session
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'NGUzMjc0MjBiYzQxMjkyZTgyZTk5ZTA2MDg2MDU1NDsd'
    # SESSION_COOKIE_DOMAIN = ''
    # SESSION_COOKIE_NAME = ''

    # database
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/python'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = False