USE Hobbyhuset;

SELECT Vare1.VNr,Vare1.Betegnelse,Vare1.Pris,Vare1.KatNr
FROM Vare AS Vare1
WHERE Vare1.Pris=
	(SELECT MIN(Vare2.Pris) 
    FROM VARE AS Vare2
	WHERE Vare1.KatNr=Vare2.KatNr)
ORDER BY KatNr;

-- alt 2, løsning ved bruk av view
CREATE VIEW BilligsteIKategori AS
(
SELECT KatNr,MIN(Pris) AS Billigste
FROM Vare
GROUP BY KatNr
);

SELECT * 
From BilligsteIKategori;

SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM Vare,BilligsteIKategori
WHERE Vare.Katnr = BilligsteIKategori.Katnr
	AND Vare.Pris = Billigste;
    
-- alt 3, BilligsteIKategori som navngitt spørring i FROM Delen
SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM VARE,(SELECT KatNr,MIN(Pris) AS Billigste
			FROM Vare
			GROUP BY KatNr) AS BiK
WHERE Vare.Katnr=BiK.KatNr
	AND Vare.Pris = BiK.Billigste;
    
    
-- spørring mot systemtabeller
USE INFORMATION_SCHEMA;

-- Denne spørringen gir oversikt over alle tabeller
-- for alle databasene
SELECT *
FROM TABLES;

-- Denne gir oversikt over alle systemtabellene
-- du kan spørre mot
SELECT *
FROM TABLES
WHERE TABLE_SCHEMA = 'information_schema';

SELECT *
FROM TABLES
WHERE TABLE_SCHEMA = 'Ansattpersonal2021';

SELECT *
FROM COLUMNS
WHERE TABLE_NAME = 'Kursdeltagelse';

SELECT *
FROM TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'Ansattpersonal2021';

SELECT *
FROM REFERENTIAL_CONSTRAINTS;

SELECT *
FROM VIEWS;

SELECT *
FROM USER_PRIVILEGES;

SELECT *
FROM STATISTICS;

SELECT *
FROM STATISTICS
WHERE TABLE_SCHEMA='Hobbyhuset';

USE Hobbyhuset;
CREATE INDEX EtternavnIDX ON Kunde(Etternavn);

USE INFORMATION_SCHEMA;
SELECT *
FROM STATISTICS
WHERE TABLE_SCHEMA='Hobbyhuset';