import os


class Config: 
    PROPAGATE_EXCEPTIONS = True
    API_Title = 'padawans portal'
    API_VERSION = 'v1'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")