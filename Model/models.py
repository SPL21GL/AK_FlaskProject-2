# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Abendveranstaltung(db.Model):
    __tablename__ = 'abendveranstaltung'

    AbendveranstaltungId = db.Column(db.Integer, primary_key=True, unique=True)
    Datum = db.Column(db.Date)
    Tische = db.Column(db.String(64), nullable=False)
    Sessel = db.Column(db.String(64), nullable=False)
    Musik = db.Column(db.String(64), nullable=False)


class Abendvgast(db.Model):
    __tablename__ = 'abendvgast'

    AbendVGastId = db.Column(db.Integer, primary_key=True, unique=True)
    AbendveranstaltungId = db.Column(db.Integer)
    GastId = db.Column(db.Integer)


class Gast(db.Model):
    __tablename__ = 'gast'

    GastId = db.Column(db.Integer, primary_key=True, unique=True)
    Nachname = db.Column(db.String(120), nullable=False)
    Vorname = db.Column(db.String(120), nullable=False)
    Lebensalter = db.Column(db.Integer, nullable=False)
    Begleitung = db.Column(db.Integer, nullable=False)


class Reservationsmitarbeiter(db.Model):
    __tablename__ = 'reservationsmitarbeiter'

    MitarbeiterId = db.Column(db.Integer, primary_key=True, unique=True)
    Nachname = db.Column(db.String(120), nullable=False)
    Vorname = db.Column(db.String(120), nullable=False)
    Arbeitszeit = db.Column(db.String(120), nullable=False)
    Lohn = db.Column(db.Numeric(10, 0), nullable=False)
