from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class AbendVdeleteForm(FlaskForm):
    AbendveranstaltungId = StringField("AbendveranstaltungId")
