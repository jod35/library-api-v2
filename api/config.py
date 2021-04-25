from decouple import config


database_user=config('DATABASE_USER')
database_password=config('DATABASE_PASSWORD')
database_name=config('DATABASE_NAME')

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=f'postgresql://{database_user}:{database_password}@localhost/{database_name}'
    DEBUG=config('DEBUG_DEV',cast=bool)
    SQLALCHEMY_ECHO=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=config('PRODUCTION_DB_URI')
    DEBUG=config('DEBUG_PROD',cast=bool)


    