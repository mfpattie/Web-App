import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost:Tuscaloosa91197!@localhost/<databasename>'
    SECRET_KEY = "\x04\x95s\xba0\xbba\xfb\xc4\xa4\xf2=\xd6Q\x11\xa5`b\x88R'\xa3\x10\x81"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    """
    # Email server configuration if you need email capabilities
    MAIL_SERVER = 'smtp.yourserver.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'your-email@example.com'
    MAIL_PASSWORD = 'your-email-password'
    """
    ADMINS = ['masonpattie@minutemetricsinc.com']
    POSTS_PER_PAGE = 25


class DevelopmentConfig(Config):
    # ... development-specific configurations
    pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # Use a separate test database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost:Tuscaloosa91197!@localhost/<databasename>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in the testing configuration
    # Example for testing purposes
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ADMINS = ['masonpattie@minutemetricsinc.com']
    POSTS_PER_PAGE = 25


class ProductionConfig(Config):
    # ... production-specific configurations
    pass
