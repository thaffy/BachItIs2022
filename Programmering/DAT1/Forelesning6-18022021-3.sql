-- Spørringer for ansattpersonal
-- NB! ikke bland INNER JOIN og WHERE til eksamen... velg én..

USE ansattpersonal2021;

-- Data i tabellen Ansatt for seg selv
SELECT *
FROM Ansatt;

-- Data i tabellen Postkatalog for seg selv
SELECT *
FROM Postkatalog;

-- Kryssproduktet av Postkatalog og Ansatt
-- Blir mye tull med denne spørringen... 30 resultater for 5 ansatte.. Bare noen få rader er korrekte (postnr stemmer overens)
-- Alle rader i postnr (6) blir kombinert med alle radene i ansatt (5) - 5*6 = 30 resultater
SELECT *
FROM Postkatalog, Ansatt;

-- Likekobling, liste over ansatte med postadresser, med WHERE-betingelse
-- Vi vil bare ha de radene hvor postnr i Postkatalog stemmer med postnr i Ansatt
SELECT *
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- med et kolonneutvalg 
-- Vi må spesifiere hvilken kolonne vi henter fra (f.eks Ansatt.Postnr) hvis den finnes i begge tabeller. Er den entydig trenger man ikke å si hvor den er fra
SELECT Ansattnr,Fornavn,Etternavn,Gateadresse,Ansatt.Postnr,Poststed
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- Likekobling, liste over ansatte med postadresser, med INNER JOIN --> jfr s 100
-- med INNER JOIN er koblingsbetingelsen flyttet fra WHERE-delen til FROM-delen
SELECT Ansattnr,Fornavn,Etternavn,Gateadresse,Ansatt.Postnr,Poststed
FROM Ansatt INNER JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;
-- !!NB!! Søknad om stryk på eksamen/ikke bestått: Ikke bruk INNER JOIN med WHERE i samme spørring.. (istedet for ON?) Bruk enten WHERE eller INNER JOIN .. ON ... 


-- Likekobling 3 tabeller, liste over ansatte med stilling og avdeling, med WHERE betingelse
SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
    
-- Den samme spørringen med INNER JOIN (Ikke Ståle sin, skrevet selv - ikke bruk, Ståle gjør dette på en annen mye mer forvirrende måte...)
SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Ansatt INNER JOIN (Stillingstype,Avdeling)
	ON Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
    -- Denne måten å gjøre det på er tydligvis feil?
    
SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Ansatt
	INNER JOIN Stillingstype
		ON Ansatt.Stillingskode=Stillingstype.Stillingskode
	INNER JOIN Avdeling
		ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;

    
-- Koble tre eller flere tabeller, først 2, "steg for steg"
SELECT Etternavn,Fornavn,Stillingsbetegnelse
-- ,Avdelingsnavn
FROM Ansatt, Stillingstype
-- ,Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
-- AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr
;

-- Ståle anbefaler WHERE for koblinger med flere tabeller: "Størst sannsynlig at resultatet blir riktig"

-- Ved bruk av INNER JOIN kan det være enda viktigere å bygge opp steg for steg
-- først ansatt mot avdeling (innereste join) før
-- stillingstype kobles mot mellomresultatet av innerste join
SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Stillingstype INNER JOIN
	(Ansatt INNER JOIN Avdeling
		ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr)
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;
    
-- alternativt med INNER JOIN
-- først ansatt mot Stillingstype (innerste JOIN) før
-- Avdeling kobles mot mellomresultatet av innerste JOIN
SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Avdeling INNER JOIN
	(Ansatt INNER JOIN Stillingstype
		ON Ansatt.Stillingskode=Stillingstype.Stillingskode)
	ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;
    
-- View/utsnitt
-- oppretting av View Ansattliste
-- Etternavn, Fornavn, Stillingstype, Avdeling med info fra de 3 tabellene.
-- Ansatt, Stillingstype, Avdeling

DROP VIEW IF EXISTS Ansattliste;

CREATE VIEW Ansattliste(Etternavn,Fornavn,Stilling,Avdeling) AS
(SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Ansatt,Stillingstype,Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr);

-- Kan så kjøre spørringer mot view'et
SELECT *
FROM Ansattliste;

-- ytre koblinger
-- ønsker også stillingsbetegnelser som ikke er i bruk (ingen har pt, i dette eksempelet "Sekretær" og "Trainee")
SELECT *
FROM Stillingstype LEFT OUTER JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;

-- ekvivalent med (samme spørreresultat, annen presentasjon)
SELECT *
FROM Ansatt RIGHT OUTER JOIN Stillingstype
	ON Ansatt.Stillingskode=Stillingstype.Stillingskode;
    
-- ønsker også avdelinger som ingen er tilknytta pt
SELECT * 
FROM Avdeling LEFT OUTER JOIN Ansatt
	ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;

-- ekvivalent med
SELECT *
FROM Ansatt RIGHT OUTER JOIN Avdeling
	ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
-- !! Obs!! Legg den tabellen som har mer data enn den andre til venstre
-- !! Bruk enten left eller right. Unngå å hoppe mellom de i f.eks samme oppgave/script/oblig osv
    
    



