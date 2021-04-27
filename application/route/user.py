import os, secrets, cloudinary.uploader, cloudinary.api, cloudinary
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from application import db, bcrypt, allowed_file, app
from application.model.user import User
from application.model.menus import Menus
from werkzeug.utils import secure_filename
from PIL import Image

user = Blueprint('user',__name__)

@user.route('/')
def userery():
    return render_template('home.html')




