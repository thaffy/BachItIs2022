DROP SCHEMA IF EXISTS testdatabase;
CREATE SCHEMA testdatabase;

USE testdatabase;

-- test av ulike datatyper
-- oppretter tabellen Datatyper
CREATE TABLE Datatyper
(
PostNr1 INTEGER,
Postnr2 CHAR(4),
Dato1 DATE,
Dato2 DATE
);

INSERT INTO Datatyper VALUES(0304,'0304','2021-02-25',20210225);

-- endring av tabellstruktur
CREATE TABLE Telefonliste
(
Mobilnr CHAR(8) PRIMARY KEY,
Fornavn CHAR(15)
);

INSERT INTO Telefonliste VALUES('93031376','Ståle');

-- Legge til en ny kolonne e-postadresse
ALTER TABLE Telefonliste ADD COLUMN epost CHAR(30);

-- oppdaterer registrert person med e-postadresse
UPDATE Telefonliste
SET epost='stale.vikhagen@usn.no'
WHERE Mobilnr='93031376';

-- Opprette ny tabell postkatalog
CREATE TABLE Postkatalog
(
Postnr CHAR(4) PRIMARY KEY,
Poststed CHAR(20) NOT NULL
);

-- legge til kolonne Postnr, som er fremmednøkkel mot Postkatalog, i Telefonliste

ALTER TABLE Telefonliste ADD COLUMN Postnr CHAR(4);
ALTER TABLE Telefonliste ADD CONSTRAINT TelefonlistePostkatalogFK FOREIGN KEY (Postnr) REFERENCES Postkatalog(Postnr);

-- legge data i Postkatalog
INSERT INTO Postkatalog VALUES('3470','Slemmestad');
INSERT INTO Postkatalog VALUES('6400','Molde');

-- legge til Postnr for registrert person
UPDATE Telefonliste
SET Postnr='3470'
WHERE Mobilnr='93031376';

-- legger til 99999999, Jens på postnr 6400, ok eller ikke? Ok
INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr) VALUES('99999999','Jens','6400');

-- legger til 44444444, Kari på postnr 7800,ok eller ikke? Ikke, fordi postnr ikke er registrert fra før i postkatalogen
INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr) VALUES('44444444','Kari','7800');

-- må legge inn 7800 Namsos i postkatalogen først
-- så kjøre insert into på nytt:
INSERT INTO Postkatalog VALUES ('7800','Namsos');
INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr) VALUES('44444444','Kari','7800');











