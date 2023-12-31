from dotenv import load_dotenv
import os
load_dotenv()

DEBUG = False
SECRET_KEY = os.getenv("PROD_APP_SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("PROD_SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_MAX_OVERFLOW = 5
SQLALCHEMY_POOL_TIMEOUT = 300
SQLALCHEMY_POOL_RECYCLE = 280