from flask import Flask
from flask_migrate import Migrate
from app.db import db
from app.views import bp
from templates.config import Config
from app.models import Employee, Position, Division, Job

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1029@localhost:5432/laba5_6"

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bp)