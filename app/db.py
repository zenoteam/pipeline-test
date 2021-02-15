import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user = 'postgres'
host = 'postgres'
database = 'postgres'
pwd = 'postgres'
port = 5432

DB_URI = f'postgresql://{user}:{pwd}@{host}:{port}/{database}'

db_config = {
    'SQLALCHEMY_DATABASE_URI': DB_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}
