import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')

os.makedirs(INSTANCE_DIR, exist_ok=True)

DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'app.db')}"