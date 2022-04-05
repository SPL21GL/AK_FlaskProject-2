from flask import Flask
from Model.models import db
from flask_wtf.csrf import CSRFProtect
import sqlalchemy
from controllers.index import index_blueprint


app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Abendveranstaltung"
db.init_app(app)

app.register_blueprint(index_blueprint)

app.run(debug=True)
