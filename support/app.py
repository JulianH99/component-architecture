from email import message
import site
import json
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


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/support/active')
def get_active_support():
    return ''


@app.route('/save-message')
def update_message():
    form_data = request.form
    if not (form_data['business'] and form_data['email'] and form_data['message']):
        flash("Error: Empty fields")
        return redirect(request.url)
    try:
        message = Message(
            business=form_data['business'],
            email=form_data['email'],
            message=form_data['message'],
        )
        db.session.add(message)
        db.session.commit()
        flash("add new message")
        return redirect('landing.html')
    except:
        return redirect(request.url)


@app.route('/support/messages')
def show_messages():
    messages = Message.query.all()
    return json.loads(messages)
