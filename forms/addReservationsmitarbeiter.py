from time import time
from tokenize import String
from MySQLdb import Date
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms import HiddenField

#from Model.models import Abendveranstaltung


class ReservationsmitarbeiterForm(FlaskForm):
    MitarbeiterId = HiddenField("MitarbeiterId")
    Nachname = StringField("Nachname")
    Vorname =  StringField("Vorname") 
    Arbeitszeit =   StringField("Arbeitszeit")
    Lohn = StringField("Lohn")