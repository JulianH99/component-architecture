from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

CORS(app)

# UPLOAD_FOLDER = os.path.join('static', 'uploads')

app.debug = True
app.secret_key = 'gPbM^#;49m9g+swb@Pl]X5qB@.tb%t'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/gardens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

try:
    from .models import *
except:
    print("Could not load models")

db.create_all()


# if not os.path.isdir(UPLOAD_FOLDER):
#    os.mkdir(UPLOAD_FOLDER)


@app.route('/support/active')
def get_active_support():
    return ''


@app.route('/save-message')
def update_message():
    form_data = request.json
    if not (form_data['business'] and form_data['email'] and form_data['message']):
        flash("Error: Empty fields")
        return jsonify({'message': 'Error: Empty fields'})
    try:
        message = Message(
            business=form_data['business'],
            email=form_data['email'],
            message=form_data['message'],
        )
        db.session.add(message)
        db.session.commit()
        flash("add new message")
        return jsonify({'message': 'add new message'})
    except:
        return jsonify({'message': 'Error: Message not save'})


@app.route('/support/messages')
def show_messages():
    messages = Message.query.all()
    return jsonify(messages)
