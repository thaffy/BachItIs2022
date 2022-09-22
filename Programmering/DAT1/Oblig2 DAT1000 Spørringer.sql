USE bysyklene;

-- b)

SELECT *
FROM Sykkel;

-- c)
SELECT Etternavn,Fornavn,Mobilnr
FROM Kunde
ORDER BY Etternavn;

-- d)
SELECT *
FROM Sykkel
WHERE Startdato >= 20180401;

-- e)
SELECT COUNT(*) AS AntallKunder
FROM Kunde;

-- f)
SELECT Etternavn,Fornavn,Kunde.Mobilnr,COUNT(Utleie.Mobilnr) AS AntallUtleier
FROM Kunde LEFT OUTER JOIN Utleie
	ON Kunde.Mobilnr = Utleie.Mobilnr
GROUP BY Etternavn,Fornavn,Kunde.Mobilnr;

-- g)
SELECT *
FROM Kunde
WHERE NOT EXISTS
	(SELECT Utleie.Mobilnr FROM Utleie
    WHERE Kunde.Mobilnr = Utleie.Mobilnr);

-- h)
SELECT *
FROM Sykkel
WHERE NOT EXISTS
	(SELECT Utleie.SykkelID FROM Utleie
    WHERE Sykkel.SykkelID = Utleie.SykkelID);
    
-- i)
INSERT INTO Kunde VALUES ('11111111','Tore','Syklesen','1111222233334444');

-- j) Lag et View som viser hvilke sykler som er tilgjengelig ved hvert sykkelstativ. Lista skal inneholde StativID, Sted og SykkelID. Kall View’et LedigeSykler.
CREATE VIEW LedigeSykler AS
(
SELECT Sykkelstativ.StativID,Sykkelstativ.Sted,Sykkel.SykkelID
FROM Sykkelstativ,Sykkel,Utleie
WHERE Sykkelstativ.StativID = Sykkel.StativID
	AND Sykkel.SykkelID = Utleie.SykkelID
    AND Innlevert IS NOT NULL
GROUP BY Sykkelstativ.StativID,Sykkelstativ.Sted,Sykkel.SykkelID
);

CREATE VIEW LedigeSyklerAmelia AS
(
SELECT Sykkel.SykkelID,Sykkel.StativID,Sykkelstativ.Sted
FROM SYKKEL LEFT OUTER JOIN Sykkelstativ
	ON Sykkel.StativID = Sykkelstativ.StativID
WHERE Sykkel.StativID IS NOT NULL);


SELECT *
FROM LedigeSykler;

SELECT * FROM LedigeSyklerAmelia;
SELECT * FROM LedigeSykler;


-- k) Lag sql-setningen for å opprette brukeren Sykkelsjef. 
CREATE USER 'Sykkelsjef' IDENTIFIED BY 'bysyklene';

-- l)Lag sql-setningen for å gi brukeren Sykkelsjef lesetilgang til View’et LedigeSykler. 
GRANT SELECT ON LedigeSykler TO 'Sykkelsjef';

-- m)
SELECT Sykkel.SykkelID,StativID,Låsnr, COUNT(Utleie.SykkelID) AS AntallUtleier
FROM Sykkel INNER JOIN Utleie
	ON Sykkel.SykkelID = Utleie.SykkelID
GROUP BY SykkelID, StativID,Låsnr
HAVING AntallUtleier >= 100
ORDER BY AntallUtleier DESC;

-- n)Lag en spørring som viser mobilnr, fornavn, etternavn og totalbeløpet for alle utleier for hver enkelt kunde. Lista skal presenteres i synkende rekkefølge med den kunden som har betalt mest i leie først. 
SELECT Kunde.Mobilnr,Fornavn,Etternavn,SUM(Beløp) AS Totalsum
FROM Kunde,Utleie
WHERE Kunde.Mobilnr = Utleie.Mobilnr
GROUP BY Kunde.Mobilnr,Fornavn,Etternavn
ORDER BY Totalsum DESC;

select * from utleie;

-- o)Lag en spørring som viser hvor mange ledige sykler som er tilgjengelig ved hvert sykkelstativ. Lista skal inneholde StativID, Sted og antall ledige sykler. 
SELECT Sykkelstativ.StativID,Sykkelstativ.Sted,COUNT(Sykkel.SykkelID) AS AntallLedigeSykler
FROM Sykkelstativ,Sykkel,Utleie
WHERE Sykkelstativ.StativID = Sykkel.StativID
	AND Sykkel.SykkelID = Utleie.SykkelID
    AND Utleie.Innlevert IS NOT NULL
GROUP BY Sykkelstativ.StativID,Sykkelstativ.Sted;


-- p)Lag en spørring som viser oversikt over hvilke kunder som leier en bysykkel akkurat nå. Lista skal inneholde Etternavn, Mobilnr, SykkelID, StartDato og starttidspunkt for utleien. 
SELECT Etternavn,Kunde.Mobilnr,Sykkel.SykkelID,StartDato,Utlevert
FROM Kunde,Sykkel,Utleie
WHERE Kunde.Mobilnr = Utleie.Mobilnr
	AND Sykkel.SykkelID = Utleie.SykkelID
    AND Innlevert IS NULL
GROUP BY Etternavn,Kunde.Mobilnr,Sykkel.SykkelID,StartDato,Utlevert;

-- q)Lag en spørring som viser hvilke sykler, med informasjon om kunde, som ikke er levert tilbake etter ett døgn. 

-- r)Lag en spørring som gir oversikt over den sykkelen/de syklene som har vært utleid flest ganger (flere kan altså ha «like mange og flest)

SELECT SykkelID, COUNT(SykkelID) AS AntallUtleier
FROM Utleie 
GROUP BY SykkelID 
HAVING COUNT(SykkelID) >= (
	SELECT COUNT(SykkelID) AS AntallUtleier
    FROM Utleie 
    GROUP BY SykkelID
    ORDER BY AntallUtleier DESC LIMIT 1);
    
    
-- q
SELECT SykkelID,Mobilnr,Utlevert,Innlevert, NOW() AS SjekkTidspunkt
FROM Utleie
WHERE Innlevert IS NULL
GROUP BY SykkelID,Mobilnr,Utlevert
	HAVING TIMESTAMPDIFF(HOUR,Utlevert,Sjekktidspunkt) > 24
;

SELECT * FROM Utleie;
INSERT INTO Utleie VALUES ('1000000001', '2021-03-24 12:45:04', '47684509', '2020-06-09 08:32:22', '105.50');
INSERT INTO Utleie VALUES ('1000000002', '2021-03-24 12:45:04', '47684509',NULL, '105.50');



SELECT Kunde.Etternavn, Utleie.Mobilnr, Utleie.SykkelID, Utleie.Utlevert
FROM Utleie LEFT OUTER JOIN Kunde 
	ON Utleie.Mobilnr=Kunde.Mobilnr
WHERE Utlevert <=NOW()
	AND Innlevert IS NULL
GROUP BY Kunde.Etternavn,Utleie.Mobilnr,Utleie.SykkelID,Utleie.Utlevert;

        


    






    
    






	








