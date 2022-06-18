from tokenize import String
from MySQLdb import Date
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms import HiddenField
from wtforms.fields import SelectField


choices = [("Klassik", "Klassik"), ("Jazz", "Jazz"), ("Schlager", "Schlager"), ("Pop", "Pop"), ("Rock",
                                                                                                "Rock"), ("Hip-Hop", "Hip-Hop"), ("Techno", "Techno"), ("Elektro", "Elektro")]


class AbendveranstaltungForm(FlaskForm):
    AbendveranstaltungId = HiddenField("AbendveranstaltungId")
    Datum = DateField("Datum")
    Tische = StringField("Tische")
    Sessel = StringField("Sessel")
    Musik = SelectField("Musik", choices=choices)
