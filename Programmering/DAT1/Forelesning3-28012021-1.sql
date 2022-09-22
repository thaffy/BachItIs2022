-- løsning av diverse oppgaver kap 2
-- oppgave 1
USE oppgave1kap2;

SELECT *
From Film;

-- g)
-- Antall filmer som ikke er til salgs (eller ikke har pris)
SELECT COUNT(*) AS IkkeTilSalgs
FROM Film
WHERE Pris IS NULL;

-- h)
-- Antall filmer under 100 kr.
SELECT COUNT(PRIS) AS BilligFilmer
FROM Film
WHERE Pris < 100;

-- i)
-- Filmer med tittel som slutter på NOW
SELECT *
FROM Film
WHERE UCASE(Tittel) LIKE '%NOW';

-- oppgave 2
-- a)
SELECT Nr, Beskrivelse
FROM Hytte
WHERE (Ukepris < 4500)
	AND (AntallSenger >= 4);
    
-- e)
SELECT COUNT(*) AS AntallHytter
FROM Hytte
WHERE AvstandAlpin < 500;

-- Utfordringer med gruppering
USE gruppering;
SELECT *
FROM Ansatt;

-- En SELECT med gruppering som er feil
SELECT Stillingskode, Lønnstrinn
FROM Ansatt
GROUP BY Stillingskode;

-- Riktig SELECT for setningen over er
SELECT Stillingskode, Lønnstrinn
FROM Ansatt
GROUP BY Stillingskode, Lønnstrinn;

-- Dersom vi vil finne antall ansatte i de ulike gruppene utvider vi setningen med en COUNT
SELECT Stillingskode, Lønnstrinn, COUNT(*) AS AntallAnsatte
FROM Ansatt
GROUP BY Stillingskode, Lønnstrinn;

-- Sammenlignet med å ha opptellingen i SQL setningen som er feil !!!
SELECT Stillingskode,Lønnstrinn,COUNT(*) AS AntallAnsatte
FROM Ansatt
GROUP BY Stillingskode;

-- Oppsummering
-- Gruppekriteriet: Pass på at det er det samme i SELECT-delen og GROUP BY
-- Det vi selekterer på og det vi grupperer på MÅ være det samme, ellers blir det feil resultat.alter
-- Hvis det er en gruppebetingelse bruker vi HAVING (ikke WHERE)

-- COUNT(*) teller alle rader vs COUNT(kolonnenavn), som ikke teller rader med NULL-merket.alter

-- "sammensatt gruppekriterie": for å unngå meningsløse spørringer er det et krav i SQL
-- at en hver kolonne som forkommer i SELECT-delen også er med i GROUP BY. (Avvik vil gi feil resultat, men ikke kjørefeil i MySQL)

-- Det er ikke tilltat å bruke mengdefunksjoner i WHERE-betingelsen.


    

