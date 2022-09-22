-- Gjennomgang utvalgte delspørsmål oppgave 1 kapittel 2
USE oppgave1kap2;

SELECT *
FROM Film;

-- a)
SELECT *
FROM Film
WHERE År = 1988;

-- d)
SELECT Tittel
FROM Film
WHERE (UPPER(Sjanger) = 'Action') OR (UPPER(Sjanger) = 'Western');

-- e)
SELECT DISTINCT Land
FROM Film
ORDER BY Land;


USE hobbyhusetkap2;

SELECT *
FROM Vare;

-- Operatorpresedens, AND/OR mot ("og/eller" i dagligtale)
-- Varer som koster under 100 kr i kategoriene bøker og keramikk

SELECT *
FROM Vare
WHERE (Pris < 100)
	AND (Kategori = 'Bøker') OR (Kategori = 'Keramikk');

-- Spørringen tolkes som, operatorpresedens
SELECT *
FROM Vare
WHERE ((Pris < 100) AND (Kategori = 'Bøker'))
	OR (Kategori = 'Keramikk');
    
-- mens den riktige spørringen er
SELECT *
FROM Vare
WHERE (Pris < 100)
	AND ((Kategori = 'Bøker') OR (Kategori = 'Keramikk'));
    
-- Spørring mot en tabell, avledet informasjon
-- Beregning av pris inkl mva
SELECT VNr, Betegnelse, Pris, Pris*1.25
FROM Vare;

-- avledet informasjon/ny kolonne kan navngis via omnavning, beskrivende navn
SELECT VNr, Betegnelse, Pris, Pris*1.25 AS PrisInklMva
FROM Vare;

-- Avrunding
SELECT Vnr, Betegnelse, Pris, ROUND(Pris*1.25,2) AS PrisInklMva
FROM Vare;

-- NB! Forskjell på ROUND (avrunding) og TRUNCATE (avkorting)
SELECT Vnr, Betegnelse, Pris,
	(Pris*1.25) AS PrisInklMva,
    2*ROUND(Pris*1.25,2) AS Dobbel,
    TRUNCATE(Pris*1.25,2) AS PrisInklMvaAvkortet
FROM Vare;

-- fortolkning
-- bokstaven i hylle viser hylleseksjon, bruker LEFT
-- til å trekke ut et gitt antall tegn fra venstre
SELECT VNr, Betegnelse, LEFT(Hylle,1) AS Hylleseksjon
FROM Vare;

-- og fjerner evt varer som ikke er hylleplasserte
SELECT VNr, Betegnelse, LEFT(Hylle,1) AS Hylleseksjon
FROM Vare
WHERE Hylle IS NOT NULL;

-- Her har vi ikke kontroll...
SELECT VNr, Betegnelse, LEFT(Hylle,1) AS Hylleseksjon
FROM Vare
WHERE Hylleseksjon IS NOT NULL;

-- Intervallsøk, flere ulikheter med AND(/OR) eller bruk av BETWEEN
SELECT *
From Vare
WHERE (Pris>=57) AND (Pris<=75.50);

SELECT *
FROM Vare
WHERE (Pris BETWEEN 57 AND 75.50);

-- Jokernotasjon/mønstersammenligning
-- NB!!! må bruke LIKE i stedet for =
-- varer som begynner på M
SELECT *
FROM Vare
WHERE Betegnelse LIKE 'M%';

-- evt, jfr forelesning 1
SELECT *
FROM Vare
WHERE UPPER(Betegnelse) LIKE 'M%';

-- alt
SELECT *
FROM Vare
WHERE UCASE(Betegnelse) LIKE 'M%';

-- varer som begynner på M
-- uten mønstersammenligning/dvs test på likhet
SELECT *
FROM Vare
WHERE UCASE(LEFT(Betegnelse,1)) = 'M';

-- Varer som inneholder marsipan i navnet
SELECT *
FROM Vare
WHERE UPPER(Betegnelse) LIKE '%MARSIPAN%';

-- Sortering
SELECT *
FROM Vare
ORDER BY Betegnelse;

-- ASC/stigende, DESC/synkende
SELECT *
FROM Vare
ORDER BY Kategori ASC, Pris DESC;

-- Mengdefunksjoner
-- Gjennomsnitt
SELECT AVG(Pris) AS GjennomsnittprisFiske
FROM Vare 
WHERE UCASE(Kategori)='FISKE';

SELECT ROUND(AVG(Pris),2) AS GjennomsnittprisFiske
FROM Vare
WHERE UCASE(Kategori)='FISKE';

-- Gruppering
-- (antall) kategorier, for å få oversikt
SELECT DISTINCT (Kategori)
FROM Vare;

-- Gjennomsnittspris pr kategori
-- SELECT og GROUP BY skal alltid være det samme
SELECT Kategori, ROUND(AVG(Pris),2) AS GjennomsnittsPris
FROM Vare
GROUP BY Kategori;

-- Utvidet med største og minste pris i hver kategori
SELECT Kategori, ROUND(AVG(Pris),2) AS GjennomsnittsPris,
	MIN(Pris) AS Billigste,
    MAX(Pris) AS Dyreste
FROM Vare
GROUP BY Kategori;

-- Opptelling, antall varer i kategoriene 'Blomsterfrø' og 'Blomsterløker'
SELECT COUNT(*) AS AntallBlomsterVarer
FROM Vare
WHERE Kategori = 'Blomsterfrø' OR Kategori = 'Blomsterløker';

SELECT COUNT(*) AS AntallBlomsterVarer
FROM Vare
WHERE UPPER(Kategori) LIKE 'BLOMSTER%';

-- Gruppebetingelser
SELECT Kategori, COUNT(*) AS AntallVarer
FROM Vare
GROUP BY Kategori
HAVING COUNT(*)>1;

SELECT Kategori, COUNT(*) AS AntallVarer
FROM Vare
GROUP BY Kategori
HAVING AntallVarer > 1;