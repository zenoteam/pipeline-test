import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DB_URI = os.environ.get("DATABASE_URI", "postgres://localhost:8000")

db_config = {
    'SQLALCHEMY_DATABASE_URI': DB_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}
