from flask import Flask, Response, render_template, request, redirect, flash, url_for, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')

app.debug = True
app.secret_key = 'gPbM^#;49m9g+swb@Pl]X5qB@.tb%t'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://gardens:gardens@db:3306/gardens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

try:
    from .models import *
except:
    print("Could not load models")

db.create_all()


# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')
CORS(api)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/supply')
def list_supply():
    supplies = Supply.query.all()
    return render_template('supply/supply.html', supplies=supplies)


@app.route('/supply/new', methods=['GET', 'POST'])
def new_supply():
    if request.method == "GET":
        return render_template('supply/new_supply.html')

    if request.method == "POST":
        form_data = request.form
        if not (form_data['sku'] and form_data['price'] and form_data['stock'] and form_data['name']):
            flash("value error")
            return redirect(request.url)
        try:
            supply = Supply(
                sku=form_data['sku'],
                name=form_data['name'],
                price_suggested=form_data['price'],
                stock=form_data['stock']
            )
            db.session.add(supply)
            db.session.commit()
            flash("added new supply")
            return redirect(url_for('list_supply'))
        except:
            flash("the sku has different")
            return redirect(request.url)


@api.get('/alive')
def api_status():
    return Response(status=200)


@api.get('/supply')
def get_products():
    products = Supply.query.all()
    return jsonify([(dict(product.as_dict())) for product in products])


app.register_blueprint(api)


if __name__ == '__main__':
    print("running")
    app.run()
