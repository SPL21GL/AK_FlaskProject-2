from tokenize import String
from MySQLdb import Date
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms import HiddenField

from Model.models import Abendveranstaltung


class AbendveranstaltungForm(FlaskForm):
    Abendveranstaltung_Id = HiddenField("AbendveranstaltungId")
    Datum = DateField("Datum")
    Tische =  StringField("Tische") 
    Sessel =   StringField("Sessel")
    Musik = StringField("Musik")