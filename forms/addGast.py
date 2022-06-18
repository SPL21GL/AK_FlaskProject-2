from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators, HiddenField
from wtforms.fields import SelectField


choices = [("1", "1"), ("2", "2"), ("3", "3")]


class GastForm(FlaskForm):
    GastID = HiddenField("GastId")
    Nachname = StringField("Nachname", [validators.InputRequired()])
    Vorname = StringField("Vorname", [validators.InputRequired()])
    Alter = StringField("Alter", [validators.InputRequired()])
    Begleitung = SelectField("Begleitung", choices=choices)


