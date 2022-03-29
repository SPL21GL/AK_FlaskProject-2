from flask import Flask, redirect
from models import db 
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/AbendVeranstaltungApp"
db.init_app(app)

#csrf = CSRFProtect(app)


#hier blueprint registrieren


app.run(debug=True)

