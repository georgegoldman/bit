import os, cloudinary
import http.client
from dotenv import load_dotenv
from flask import Flask, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

load_dotenv()

cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key = os.environ.get('CLOUDINARY_API_KEY'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET')
)

app = Flask(__name__)

# UPLOAD_FOLDER = '/home/yashuayaweh/Documents/PROGRAMMING/lifeat/application/static/imgs/menu'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.'in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


bcrypt = Bcrypt(app)

app.config['DEBUG'] = False
if os.environ.get('FLASK_ENV') == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print(f'ENV is set to: {app.config["ENV"]}')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
Migrate = Migrate(app, db)
login_manager = LoginManager(app)

from .model.user import User
from .model.menus import Menus

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager.login_view = '/'
login_manager.login_message = "Please login"

from .route import user
app.register_blueprint(user.user)