USE Hobbyhuset;

SELECT *
FROM Gullklubblista;

-- med de mestkjøpende/VIP'ene først
SELECT *
FROM Gullklubblista
ORDER BY Antallbestillinger DESC;

-- Gullklubblista som en spørring uten bruk av view
SELECT Ordre.KNr,Fornavn,Etternavn,Adresse,Postnr,Poststed,COUNT(Ordre.KNr) AS AntallBestillinger
FROM Ordre,Kunde,Poststed
WHERE (Ordre.KNr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr)
GROUP BY Ordre.KNr,Fornavn,Etternavn,Adresse,Postnr,Poststed
HAVING AntallBestillinger>=10
ORDER BY AntallBestillinger DESC;

-- Egenkobling
USE egenkobling;
SELECT *
FROM Ansatt;

SELECT Ansatte.AnsNr,Ansatte.Fornavn,Ansatte.Etternavn,Lederen.Etternavn AS HarSomLeder
FROM (Ansatt AS Ansatte) LEFT OUTER JOIN (Ansatt AS Lederen)
ON Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.Fornavn;

USE Hobbyhuset;

SELECT VNr,Betegnelse,Pris
FROM Vare
WHERE Pris<(SELECT AVG(PRIS) FROM VARE);

-- finne de(n) billigste varen(e) i hver kategori
-- vekselvirkende del-spørring
SELECT DISTINCT (KatNr)
FROM Vare;

SELECT Vare1.VNr,Vare1.Betegnelse,Vare1.Pris,Vare1.KatNr
FROM Vare AS Vare1
WHERE Vare1.Pris=
	(SELECT MIN(Vare2.Pris) 
    FROM VARE AS Vare2
	WHERE Vare1.KatNr=Vare2.KatNr)
ORDER BY KatNr;

-- prøv selv
-- billigste vare i hver kategori, ved bruk av view
-- BilligsteIKategori som navngitt spørring og spørring i FROM-delen


