from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from forms.addGast import GastForm
from Model.models import Gast, db

gast_blueprint = Blueprint('gast_blueprint', __name__)


@gast_blueprint.route("/gaeste")
def gaeste():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    gaeste = session.query(Gast).all()
    return render_template("gaeste/gaeste.html",gaeste= gaeste)

@gast_blueprint.route("/gaeste/add", methods=["GET", "POST"])
def gast_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    add_gast_form = GastForm()

    if request.method == 'POST':

        if add_gast_form.validate_on_submit():
            
                new_gast = Gast()

                new_gast.Nachname = add_gast_form.Nachname.data
                new_gast.Vorname = add_gast_form.Vorname.data
                new_gast.Lebensalter = add_gast_form.Alter.data
                new_gast.Begleitung = add_gast_form.Begleitung.data
            
                db.session.add(new_gast)
                db.session.commit()

                return redirect("/gaeste")
        else:
            return render_template("gaeste/add_gaeste.html", gast=Gast, form=add_gast_form)
    else:
        return render_template("gaeste/add_gaeste.html", gast=Gast, form=add_gast_form)
