import os
from dotenv import load_dotenv

sqlite_uri = os.path.abspath("app/database/database.db")
project_root = os.getcwd()
load_dotenv(os.path.join(project_root, '.env'))


class Config(object):
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + sqlite_uri
