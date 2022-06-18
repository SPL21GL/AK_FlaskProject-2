from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from forms.addReservationsmitarbeiter import ReservationsmitarbeiterForm
from Model.models import Reservationsmitarbeiter, db
from forms.deletereservationsmitarbeiter import MitarbeiterDeleteForm

reservationsmitarbeiter_blueprint = Blueprint(
    'reservationsmitarbeiter_blueprint', __name__)
1


@reservationsmitarbeiter_blueprint.route("/reservierungsmitarbeiter")
def reservationsmitarbeiter():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    reservationsmitarbeiter = session.query(Reservationsmitarbeiter).all()
    return render_template("reservationsmitarbeiter/reservationsmitarbeiter.html", reservationsmitarbeiter=reservationsmitarbeiter)


@reservationsmitarbeiter_blueprint.route("/reservationsmitarbeiter/add", methods=["GET", "POST"])
def reservationsmitarbeiter_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    add_reservationsmitarbeiter_form = ReservationsmitarbeiterForm()

    if request.method == 'POST':

        if add_reservationsmitarbeiter_form.validate_on_submit():
            new_reservationsmitarbeiter = Reservationsmitarbeiter()

            new_reservationsmitarbeiter.Nachname = add_reservationsmitarbeiter_form.Nachname.data
            new_reservationsmitarbeiter.Vorname = add_reservationsmitarbeiter_form.Vorname.data
            new_reservationsmitarbeiter.Arbeitszeit = add_reservationsmitarbeiter_form.Arbeitszeit.data
            new_reservationsmitarbeiter.Lohn = add_reservationsmitarbeiter_form.Lohn.data

            db.session.add(new_reservationsmitarbeiter)
            db.session.commit()
            return redirect("/reservierungsmitarbeiter")
    else:
        return render_template("reservationsmitarbeiter/add_reservationsmitarbeiter.html", reservationsmitarbeite=Reservationsmitarbeiter, form=add_reservationsmitarbeiter_form)


@reservationsmitarbeiter_blueprint.route("/reservationsmitarbeiter/edit", methods=["GET", "POST"])
def reservierungsmitarbeiter_edit():

    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_reservierungsmitarbeiter = ReservationsmitarbeiterForm()

    if request.method == "POST":
        if edit_reservierungsmitarbeiter.validate_on_submit():

            Mitarbeiter_to_edit = db.session.query(Reservationsmitarbeiter).filter(
                Reservationsmitarbeiter.MitarbeiterId == edit_reservierungsmitarbeiter.MitarbeiterId.data).first()

            Mitarbeiter_to_edit.Nachname = edit_reservierungsmitarbeiter.Nachname.data
            Mitarbeiter_to_edit.Vorname = edit_reservierungsmitarbeiter.Vorname.data
            Mitarbeiter_to_edit.Arbeitszeit = edit_reservierungsmitarbeiter.Arbeitszeit.data
            Mitarbeiter_to_edit.Lohn = edit_reservierungsmitarbeiter.Lohn.data

            db.session.commit()

            return redirect("/reservierungsmitarbeiter")
    else:
        MitarbeiterId = request.args["MitarbeiterId"]
        reservierungsmitarbeiter_to_edit = db.session.query(Reservationsmitarbeiter).filter(
            Reservationsmitarbeiter.MitarbeiterId == MitarbeiterId).first()

        edit_reservierungsmitarbeiter.MitarbeiterId.data = reservierungsmitarbeiter_to_edit.MitarbeiterId
        edit_reservierungsmitarbeiter.Nachname.data = reservierungsmitarbeiter_to_edit.Nachname
        edit_reservierungsmitarbeiter.Vorname.data = reservierungsmitarbeiter_to_edit.Vorname
        edit_reservierungsmitarbeiter.Arbeitszeit.data = reservierungsmitarbeiter_to_edit.Arbeitszeit
        edit_reservierungsmitarbeiter.Lohn.data = reservierungsmitarbeiter_to_edit.Lohn

    return render_template("reservationsmitarbeiter/edit_reservationsmitarbeiter.html", form=edit_reservierungsmitarbeiter)


@reservationsmitarbeiter_blueprint.route("/reservationsmitarbeiter/delete", methods=["post"])
def deleteReservationsmitarbeiter():
    delete_Mitarbeiter_form_list = MitarbeiterDeleteForm()
    if delete_Mitarbeiter_form_list.validate_on_submit():

        MitarbeiterId_to_delete = delete_Mitarbeiter_form_list.MitarbeiterId.data
        Mitarbeiter_to_delete = db.session.query(Reservationsmitarbeiter).filter(
            Reservationsmitarbeiter.MitarbeiterId == MitarbeiterId_to_delete)
        Mitarbeiter_to_delete.delete()
        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Mitarbeiter with id {MitarbeiterId_to_delete} has been deleted")

    return redirect("/reservierungsmitarbeiter")
