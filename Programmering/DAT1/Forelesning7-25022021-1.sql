-- Skript for basisstruktur ansattpersonal2021
-- utvidet med skranker, (NOT NULL-merker). forelesning 6 - 18.02
-- Ikke tillate NULL-merke, godkjente verdier
-- ny utvidelse: skranker for masseoppdateringer
-- Obs! Primærnøkler regnes som NOT NULL automatisk, så det er bare satt på NOT NULL på attributter som ikke er primærnøkkel.

DROP SCHEMA IF EXISTS ansattpersonal2021;

CREATE SCHEMA ansattpersonal2021;

USE ansattpersonal2021;

-- oppretter tabeller, runde (1)

CREATE TABLE Stillingstype
(
Stillingskode CHAR(4),
Stillingsbetegnelse CHAR(20) NOT NULL,
CONSTRAINT StillingstypePK PRIMARY KEY(Stillingskode)
);

CREATE TABLE Avdeling
(
Avdelingsnr CHAR(4),
Avdelingsnavn CHAR(20) NOT NULL,
CONSTRAINT AvdelingPK PRIMARY KEY(Avdelingsnr)
);

CREATE TABLE Kurs
(
Kursnr CHAR(4),
Kursnavn CHAR(20) NOT NULL,
CONSTRAINT KursPK PRIMARY KEY(Kursnr)
);

CREATE TABLE Postkatalog
(
Postnr CHAR(4),
Poststed CHAR(20) NOT NULL,
CONSTRAINT PostkatalogPK PRIMARY KEY(Postnr)
);

-- oppretter tabeller runde (2)

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(15) NOT NULL,
Etternavn CHAR(20) NOT NULL,
Gateadresse CHAR(25),
Telefonnr CHAR(8) NOT NULL,
Stillingskode CHAR(4),
Avdelingsnr CHAR(4),
Postnr CHAR(4),
CONSTRAINT AnsattPK PRIMARY KEY(Ansattnr),
CONSTRAINT AnsattStillingstypeFK FOREIGN KEY(Stillingskode) REFERENCES Stillingstype(Stillingskode),
CONSTRAINT AnsattAvdelingFK FOREIGN KEY(Avdelingsnr) REFERENCES Avdeling(Avdelingsnr) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT AnsattPostkatalogFK FOREIGN KEY(Postnr) REFERENCES Postkatalog(Postnr)
);

-- oppretter tabeller runde (3)

-- (CHECK attributtnavn IN ('Verdi','verdi2')) = Inndatakontroll i SQL
CREATE TABLE Kursdeltagelse
(
Ansattnr CHAR(4),
Kursnr CHAR(4),
Dato DATE,
Vurdering CHAR(20),
CONSTRAINT KursdeltagelsePK PRIMARY KEY(Ansattnr,Kursnr,Dato),
CONSTRAINT KursdeltagelseAnsattFK FOREIGN KEY(Ansattnr) REFERENCES Ansatt(Ansattnr),
CONSTRAINT KursdeltagelseKursFK FOREIGN KEY(Kursnr) REFERENCES Kurs(Kursnr),
CONSTRAINT VurderingsRegel CHECK (Vurdering IN ('Bestått','Ikke bestått','Gjennomført','Ikke møtt'))
);


