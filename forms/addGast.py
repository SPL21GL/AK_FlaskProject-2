from tokenize import String
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import HiddenField


class GastForm(FlaskForm):
    GastID = HiddenField("GastID")
    Nachname = StringField("Nachname")
    Vorname =  StringField("Vorname") 
    Alter =   StringField("Alter")
    Begleitung = StringField("Begleitung")