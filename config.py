from flask_sqlalchemy import SQLAlchemy
from app import app


db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///structure.db"

db.init_app(app)
