from operator import imod
from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import flask_sqlalchemy
from forms.addAbendveranstaltungen import AbendveranstaltungForm
from Model.models import Abendveranstaltung, Abendveranstaltung, db

abendveranstaltungen_blueprint = Blueprint('abendveranstaltungen_blueprint', __name__)


@abendveranstaltungen_blueprint.route("")
def abendveranstaltungen():
    
    return render_template("")


@abendveranstaltungen_blueprint.route("", methods=["GET", "POST"])
def gast_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    add_abendveranstaltungen_form = AbendveranstaltungForm()

    if request.method == 'POST':
 
        if add_abendveranstaltungen_form.validate_on_submit():
                new_abendveranstaltungen = Abendveranstaltung()

                new_abendveranstaltungen.Datum = add_abendveranstaltungen_form.Datum.data
                new_abendveranstaltungen.Tische = add_abendveranstaltungen_form.Tische.data
                new_abendveranstaltungen.Sessel = add_abendveranstaltungen_form.Sessel.data
                new_abendveranstaltungen.Musik = add_abendveranstaltungen_form.Musik.data
            

                db.session.add(new_abendveranstaltungen)
                db.session.commit()

                return redirect("/gäste")
        #else:
       #     return render_template("abendveranstaltungen/abendveranstaltungen.html", Abendveranstaltung=Abendveranstaltung, form=add_abendveranstaltungen_form)
   # else:
       # return render_template("abendveranstaltungen/abendveranstaltungen.html", Abendveranstaltung=Abendveranstaltung, form=add_abendveranstaltungen_form)
