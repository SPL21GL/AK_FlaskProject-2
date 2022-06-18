from tokenize import String
from MySQLdb import Date
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms import HiddenField


class AbendveranstaltungForm(FlaskForm):
    AbendveranstaltungId = HiddenField("AbendveranstaltungId")
    Datum = DateField("Datum")
    Tische = StringField("Tische")
    Sessel = StringField("Sessel")
    Musik = StringField("Musik")
