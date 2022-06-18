create database if not exists AbendVeranstaltungApp;
use AbendVeranstaltungApp;

create table if not exists Abendveranstaltung
(
AbendveranstaltungId int auto_increment unique key primary key,
Datum date not null,
Tische varchar(64) not null,
Sessel varchar(64) not null,
Musik varchar(64) not null
);

create table if not exists Gast
(
GastId int auto_increment unique key primary key,
Nachname varchar(120) not null,
Vorname varchar(120) not null,
Lebensalter int not null,
Begleitung int not null
);

create table if not exists  AbendVGast
(
AbendVGastId int auto_increment unique key primary key, 
AbendveranstaltungId int,
GastId int
);

create table if not exists Reservationsmitarbeiter
(
MitarbeiterId int auto_increment unique key primary key,
Nachname varchar(120) not null,
Vorname varchar(120) not null,
Arbeitszeit time not null,
Lohn decimal not null
);
