import site
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')

app.debug = True
app.secret_key = 'gPbM^#;49m9g+swb@Pl]X5qB@.tb%t'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gardens:gardens@db:3306/gardens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

try:
    from .models import *
except:
    print("Could not load models")

db.create_all()


if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)


@app.get('/support/active')
def get_active_support():
    return ''


@app.post('/save-message')
def update_message():
    return ''


@app.get('/support/messages')
def show_messages():
    return ''
