from flask import redirect, request, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from forms.addReservationsmitarbeiter import ReservationsmitarbeiterForm
from Model.models import Reservationsmitarbeiter, db

reservationsmitarbeiter_blueprint = Blueprint('reservationsmitarbeiter_blueprint', __name__)


@reservationsmitarbeiter_blueprint.route("/reservationsmitabeiter")
def reservationsmitarbeiter():

    return render_template("/Reservationsmitarbeiter/reservationsmitarbeiter.html")


@reservationsmitarbeiter_blueprint.route("/Reservationsmitarbeiter/add", methods=["GET", "POST"])
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
            return redirect("/reservationsmitarbeiter")
        else:
            return render_template("reservationsmitarbeiter/add_reservationsmitarbeiter.html", reservationsmitarbeiter=Reservationsmitarbeiter, form=add_reservationsmitarbeiter_form)
    else:
        return render_template("reservationsmitarbeiter/add_reservationsmitarbeiter.html", reservationsmitarbeite=Reservationsmitarbeiter, form=add_reservationsmitarbeiter_form)
