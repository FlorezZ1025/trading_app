from flask import Blueprint, Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from routes.auth_routes import auth_bp
from utils.db import db
from config import Config


app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend


app.config.from_object(Config)

api_bp = Blueprint('api', __name__, url_prefix='/api')

#Se registran las blueprints
api_bp.register_blueprint(auth_bp)

app.register_blueprint(api_bp)

db.init_app(app)

with app.app_context():
    db.create_all()
   