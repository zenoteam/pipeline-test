import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user = os.environ.get('POSTGRES_USER', 'postgres')
host = os.environ.get('POSTGRES_HOST', 'postgres')
database = os.environ('POSTGRES_DB', 'postgres')
pwd = os.environ('POSTGRES_PASSWORD', 'postgres')
port = os.environ.get('POSTGRES_PORT', '5432')

DB_URI = 'postgresql://{user}:{pwd}@{host}:{port}/{database}'

db_config = {
    'SQLALCHEMY_DATABASE_URI': DB_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}
