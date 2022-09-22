USE ansattpersonal2021;

SELECT *
FROM Ansattliste
ORDER BY Etternavn;

-- kryssprodukt ved bruk av INNER JOIN (uten ON)
SELECT *
FROM Ansatt INNER JOIN Postkatalog;

-- kryssproduktet ved fjerning av nøkkelordet INNER (dvs en JOIN er en INNER JOIN)
SELECT *
FROM Ansatt JOIN Postkatalog;


-- likekobling
-- liste over ansatt med postadresser, med INNER JOIN og fjerning av nøkkelordet INNER
SELECT Ansattnr,Fornavn,Etternavn,Gateadresse,Ansatt.Postnr,Poststed
FROM Ansatt JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;
    
-- og videre med kortvarianten USING
SELECT Ansattnr,Fornavn,Etternavn,Gateadresse,Ansatt.Postnr,Poststed
FROM Ansatt JOIN Postkatalog
	USING(Postnr);
    
-- og med tre tabeller får vi (JOIN og USING)
SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Stillingstype JOIN
	(Ansatt JOIN Avdeling
		USING(Avdelingsnr))
	USING(Stillingskode);
    
-- ytre koblinger
-- tilsvarende kan nøkkelordet OUTER ved LEFT OUTER JOIN og RIGHT OUTER JOIN
-- dvs LEFT JOIN er en LEFT OUTER JOIN
SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;
    
-- og ved bruk av USING på betingelse/kobling
SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	USING(Stillingskode);


-- introduksjon til del-spørringer, del-spørringer i betingelser
USE Hobbyhuset;
SELECT *
FROM Kunde;

-- hvem har "bestilt varer"? dvs minst én ordre
SELECT *
FROM Ordre;

SELECT *
FROM Kunde
WHERE KNr IN(SELECT KNr FROM Ordre);

-- kunder som aldri har bestilt, ikke bestilt noe noen gang
SELECT *
FROM Kunde
WHERE KNr NOT IN(SELECT KNr FROM Ordre);

-- View'et GodeKunder
CREATE VIEW GodeKunder AS (
SELECT *
FROM Kunde
WHERE KNr IN
	(SELECT KNr FROM Ordre)
);

-- spørre mot View'et i stedet
SELECT *
FROM GodeKunder;

-- videre arbeid/forberedelser forelesning 8
-- Gullklubben, spørring og senere VIEW for å plukke ut kunder med 10 eller flere bestillinger
-- Gullklubblista, "liste til sjefen" med informasjon om alle kunder i Gullklubben


















