from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/codigo_18_backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'my_secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
