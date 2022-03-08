

import site
from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')

app.debug = True
app.secret_key = 'gPbM^#;49m9g+swb@Pl]X5qB@.tb%t'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/gardens'
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


@app.get('/')
def index():

    site_configuration = Site.query.get(1)

    return render_template('home.html', site_configuration=site_configuration)


@app.post('/site-config')
def update_site_configuration():
    form_data = request.form
    if not form_data['site-name']:
        flash('Site name cannot be empty', 'error')
        return redirect(url_for('index'))

    site_conf = Site.query.get(1)

    if not site_conf:
        site_conf = Site(name=form_data['site-name'])
        db.session.add(site_conf)
    else:
        site_conf.name = form_data['site-name']
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/banner', methods=['GET', 'POST'])
def show_banner_configuration():
    if request.method == 'GET':
        banner_configuration = Banner.query.get(1)
        return render_template('banner.html', banner_configuration=banner_configuration)

    if request.method == 'POST':
        form_data = request.form
        background_image = request.files['banner-background']
        print(form_data)
        print(background_image)

        if not (form_data['banner-title'] and background_image):
            flash('Banner title and banner background must have a value')
            return redirect(request.url)

        filename = secure_filename(background_image.filename)
        path_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        background_image.save(path_filename)

        banner_configuration = Banner.query.get(1)

        if not banner_configuration:
            banner_configuration = Banner(
                title=form_data['banner-title'], description=form_data['banner-description'], background_image=path_filename)
            db.session.add(banner_configuration)
        else:
            banner_configuration.title = form_data['banner-title']
            banner_configuration.description = form_data['banner-description']
            banner_configuration.background_image = f'/static/uploads/{filename}'

        db.session.commit()

        return redirect(request.url)


if __name__ == '__main__':
    print("running")
    app.run()
