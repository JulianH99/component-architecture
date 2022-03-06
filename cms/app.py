

import site
from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True
app.secret_key = 'gPbM^#;49m9g+swb@Pl]X5qB@.tb%t'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/gardens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

try:
    from .models import *
except:
    print("Could not load models")

db.create_all()


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

    print(site_conf)

    if not site_conf:
        site_conf = Site(name=form_data['site-name'])
        db.session.add(site_conf)
    else:
        site_conf.name = form_data['site-name']
    db.session.commit()

    return redirect(url_for('index'))


@app.get('/banner')
def show_banner_configuration():
    return jsonify(Banner.query.all())
