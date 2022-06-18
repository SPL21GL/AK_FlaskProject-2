from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from forms.addAbendveranstaltungen import AbendveranstaltungForm
from Model.models import Abendveranstaltung, db
from forms.deleteAbendveranstaltung import AbendVdeleteForm

abendveranstaltungen_blueprint = Blueprint(
    'abendveranstaltungen_blueprint', __name__)


@abendveranstaltungen_blueprint.route("/abendveranstaltungen")
def abendveranstaltungen():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    abendveranstaltungen = session.query(Abendveranstaltung).all()
    return render_template("abendveranstaltugen/abendveranstaltungen.html", abendveranstaltungen=abendveranstaltungen)


@abendveranstaltungen_blueprint.route("/abendveranstaltungen/add", methods=["GET", "POST"])
def abendveranstaltungen_add():
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

            return redirect("/abendveranstaltungen")
    else:
        return render_template("abendveranstaltugen/add_abendveranstaltung.html", abendveranstaltung=Abendveranstaltung, form=add_abendveranstaltungen_form)


@abendveranstaltungen_blueprint.route("/abendveranstaltungen/edit", methods=["GET", "POST"])
def abendveranstaltung_edit():

    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_abendveranstaltung = AbendveranstaltungForm()

    if request.method == "POST":
        if edit_abendveranstaltung.validate_on_submit():

            abendV_to_edit = db.session.query(Abendveranstaltung).filter(
                Abendveranstaltung.AbendveranstaltungId == edit_abendveranstaltung.AbendveranstaltungId.data).first()

            abendV_to_edit.Datum = edit_abendveranstaltung.Datum.data
            abendV_to_edit.Tische = edit_abendveranstaltung.Tische.data
            abendV_to_edit.Sessel = edit_abendveranstaltung.Sessel.data
            abendV_to_edit.Musik = edit_abendveranstaltung.Musik.data

            db.session.commit()

            return redirect("/abendveranstaltungen")
    else:
        AbendveranstaltungId = request.args["AbendveranstaltungId"]
        abendV_to_edit = db.session.query(Abendveranstaltung).filter(
            Abendveranstaltung.AbendveranstaltungId == AbendveranstaltungId).first()

        edit_abendveranstaltung.AbendveranstaltungId.data = abendV_to_edit.AbendveranstaltungId
        edit_abendveranstaltung.Datum.data = abendV_to_edit.Datum
        edit_abendveranstaltung.Tische.data = abendV_to_edit.Tische
        edit_abendveranstaltung.Sessel.data = abendV_to_edit.Sessel
        edit_abendveranstaltung.Musik.data = abendV_to_edit.Musik

    return render_template("abendveranstaltugen/edit_abendveranstaltung.html", form=edit_abendveranstaltung)


@abendveranstaltungen_blueprint.route("/abendveranstaltugen/delete", methods=["post"])
def deleteAbendveranstaltungen():
    delete_abendV_form_list = AbendVdeleteForm()
    if delete_abendV_form_list.validate_on_submit():

        AbendveranstaltungId_to_delete = delete_abendV_form_list.AbendveranstaltungId.data
        AbendV_to_delete = db.session.query(Abendveranstaltung).filter(
            Abendveranstaltung.AbendveranstaltungId == AbendveranstaltungId_to_delete)
        AbendV_to_delete.delete()
        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Abendveranstaltung with id {AbendveranstaltungId_to_delete} has been deleted")

    return redirect("/abendveranstaltungen")    
