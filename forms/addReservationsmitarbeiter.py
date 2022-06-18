from time import time
from tokenize import String
from MySQLdb import Date
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms import HiddenField
from wtforms.fields import SelectField

choices = [("4:00:00", "4:00:00"), ("8:00:00", "8:00:00"),
           ("10:00:00", "10:00:00")]


class ReservationsmitarbeiterForm(FlaskForm):
    MitarbeiterId = HiddenField("MitarbeiterId")
    Nachname = StringField("Nachname")
    Vorname = StringField("Vorname")
    Arbeitszeit = SelectField("Arbeitszeit", choices=choices)
    Lohn = StringField("Lohn")
