from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class GeasteDeleteForm(FlaskForm):
    GastId = StringField("GastId")
