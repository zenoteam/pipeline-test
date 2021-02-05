import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user = os.environ['POSTGRES_USER']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
pwd = os.environ['POSTGRES_PASSWORD']
port = os.environ['POSTGRES_PORT']

DB_URI = 'postgresql://{user}:{pwd}@{host}:{port}/{database}'

db_config = {
    'SQLALCHEMY_DATABASE_URI': DB_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}
