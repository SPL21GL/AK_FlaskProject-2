from flask import redirect, request, flash, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from forms.addGast import GastForm
from Model.models import Gast, db
from forms.deleteGaeste import GeasteDeleteForm

gast_blueprint = Blueprint('gast_blueprint', __name__)


@gast_blueprint.route("/gaeste")
def gaeste():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    gaeste = session.query(Gast).all()
    return render_template("gaeste/gaeste.html", gaeste=gaeste)


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


@gast_blueprint.route("/gaeste/edit", methods=["GET", "POST"])
def gast_edit():

    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_gast = GastForm()

    if request.method == "POST":
        if edit_gast.validate_on_submit():

            gast_to_edit = db.session.query(Gast).filter(
                Gast.GastId == edit_gast.GastID.data).first()

            gast_to_edit.Nachname = edit_gast.Nachname.data
            gast_to_edit.Vorname = edit_gast.Vorname.data
            gast_to_edit.Lebensalter = edit_gast.Alter.data
            gast_to_edit.Begleitung = edit_gast.Begleitung.data

            db.session.commit()

            return redirect("/gaeste")
    else:
        Gastid = request.args["GastId"]
        gast_to_edit = db.session.query(Gast).filter(
            Gast.GastId == Gastid).first()

        edit_gast.GastID.data = gast_to_edit.GastId
        edit_gast.Nachname.data = gast_to_edit.Nachname
        edit_gast.Vorname.data = gast_to_edit.Vorname
        edit_gast.Alter.data = gast_to_edit.Lebensalter
        edit_gast.Begleitung.data = gast_to_edit.Begleitung

        return render_template("gaeste/edit_gaeste.html", form=edit_gast)

    return render_template("gaeste/edit_gaeste.html", form=edit_gast)


@gast_blueprint.route("/gaeste/delete", methods=["post"])
def deleteGast():
    delete_gast_form_list = GeasteDeleteForm()
    if delete_gast_form_list.validate_on_submit():

        GastId_to_delete = delete_gast_form_list.GastId.data
        Gast_to_delete = db.session.query(Gast).filter(
            Gast.GastId == GastId_to_delete)
        Gast_to_delete.delete()
        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Gast with id {GastId_to_delete} has been deleted")

    return redirect("/gaeste")
