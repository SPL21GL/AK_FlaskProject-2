from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField

class MitarbeiterDeleteForm(FlaskForm):
    MitarbeiterId = StringField("MitarbeiterId")