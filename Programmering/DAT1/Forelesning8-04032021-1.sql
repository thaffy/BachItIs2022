-- Algoritmeforklaringer
USE Hobbyhuset;
-- Første SELECT'n s102
SELECT Ordre.*,Fornavn,Etternavn,Poststed
FROM Ordre,Kunde,Poststed
WHERE Ordre.KNr=Kunde.KNr
	AND Kunde.PostNr=Poststed.PostNr;
    
-- Siste SELECT'n s103 (Alltid grupper på alt det man select'er.
SELECT Kunde.KNr,Etternavn,COUNT(*) AS AntallOrdre
FROM Kunde,Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr,Etternavn;

-- utvidet med gruppebetingelse, kun de kundene med 10 eller flere ordre
SELECT Kunde.KNr,Etternavn,COUNT(*) AS AntallOrdre
FROM Kunde,Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr,Etternavn
HAVING AntallOrdre>=10;

-- Kortnavn/alias
SELECT K.KNr,Etternavn,COUNT(*) AS AntallOrdre
FROM Kunde AS K,Ordre AS O
WHERE K.KNr=O.KNr
GROUP BY K.KNr,Etternavn
HAVING AntallOrdre>=10;

-- egenkobling
USE egenkobling;
SELECT *
FROM Ansatt;

-- for å finne navnet på lederen til alle ansatte kan vi koble tabellen ansatt med seg selv
-- Da MÅ vi bruke kortnavn på tabellene
-- alle ansatte med navn på leder
SELECT Ansatte.AnsNr,Ansatte.Fornavn,Ansatte.Etternavn,Lederen.Etternavn AS HarSomLeder
FROM Ansatt AS Ansatte, Ansatt AS Lederen
WHERE Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.Fornavn;

-- prøv selv, hva med de ansatte som ikke har leder? (OUTER JOIN)


-- til egenarbeid
-- View til produksjon av salgsrapporter
USE Hobbyhuset;
CREATE VIEW Salg AS
(
SELECT OL.*,V.Betegnelse,K.Navn AS Kategori,O.Ordredato,O.KNr
FROM Ordre AS O,
	Ordrelinje AS OL,
	Vare AS V,
    Kategori AS K
WHERE OL.OrdreNr=O.Ordrenr
	AND OL.VNr=V.VNr
    AND V.KatNr=K.KatNr
);

SELECT *
FROM Salg;

SELECT *
FROM Ordrelinje;

-- egenarbeid, lag ulike salgsrapporter

-- kunder uten bestillinger ved bruk av NOT EXISTS
SELECT *
FROM Kunde
WHERE NOT EXISTS
	(SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);

-- Kunder med bestillinger ved bruk av EXISTS
SELECT *
FROM Kunde
WHERE EXISTS
	(SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);
    
-- leksa fra forelesning 7
-- Gullklubben, spørring og senere view for å plukke ut kunder med 10 eller flere bestillinger
-- Gullklubblista, "liste til sjefen" med informasjon om alle kunder i gullklubben
-- med infoooooooooooooo om alle kunder i "Gullklubben" basert på viewet og tabellene kunde og Poststed
USE Hobbyhuset;
-- Gullklubben og Gullklubblista
SELECT KNr,COUNT(*) AS AntallBestillinger
FROM Ordre
GROUP BY KNr
HAVING Antallbestillinger>=10;

CREATE VIEW Gullklubben AS
(
SELECT KNr,COUNT(*) AS AntallBestillinger
FROM Ordre
GROUP BY KNr
HAVING Antallbestillinger>=10
);

-- Gullklubblista
SELECT Gullklubben.KNr,Fornavn,Etternavn,Kunde.PostNr,Poststed,Antallbestillinger
FROM Gullklubben,Kunde,Poststed
WHERE Gullklubben.KNr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr;

-- som VIEW
CREATE VIEW Gullklubblista AS
(
SELECT Gullklubben.KNr,Fornavn,Etternavn,Kunde.PostNr,Poststed,Antallbestillinger
FROM Gullklubben,Kunde,Poststed
WHERE Gullklubben.KNr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr
);

-- spørre mot VIEW'et
SELECT *
FROM Gullklubblista;

-- oppgave:
-- Gullklubblista som én spørring uten bruk av VIEW
-- tips: Pass på gruppekriteriet
SELECT Kunde.KNr,Fornavn,Etternavn,Kunde.PostNr,Poststed,COUNT(*) AS AntallBestillinger
FROM Kunde,Ordre,Poststed
WHERE Kunde.KNr=Ordre.KNr
	AND Kunde.PostNr=Poststed.PostNr
GROUP BY Kunde.KNr,Fornavn,Etternavn,Kunde.PostNr,Poststed
HAVING AntallBestillinger>=10
ORDER BY AntallBestillinger DESC;

--  ! ikke bruk natural join !
USE ansattpersonal2021;
SELECT *
FROM Ansatt NATURAL JOIN Stillingstype;

SELECT *
FROM Ansatt NATURAL JOIN Stillingstype NATURAL JOIN Avdeling;
-- ! ikke bruk natural join !





    