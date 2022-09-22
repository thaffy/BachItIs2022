USE hobbyhusetkap2;

-- Hele tabellen
SELECT *
FROM Vare;

-- Hele tabellen sortert på varenr
SELECT *
FROM Vare
ORDER BY Vnr;

-- Hele varesortimentet, ingen identiske rader
SELECT Vnr, Betegnelse
FROM Vare;

-- Noen spørringer kan gi like rader
SELECT Kategori
FROM Vare;

-- Fjerner dubletter (duplikater)
SELECT DISTINCT Kategori
FROM Vare;

-- Plukke ut varer i katagorien fiske
SELECT *
FROM Vare
WHERE Kategori='Fiske';

-- Standaren er case-sensitiv, der er ikke MySQL
SELECT *
FROM Vare
WHERE Kategori='fiske';

-- Generell løsning - Plukker ut alle "fiske" uavhengig av hvordan det er skrevet med store/små bokstaver, så lenge det er skrevet fiske korrekt.
SELECT *
FROM Vare
WHERE UPPER(Kategori)='FISKE';

-- Talluttrykk
SELECT *
FROM Vare
WHERE Pris < 100;

SELECT *
FROM Vare
WHERE Pris >= 100;

SELECT *
FROM Vare
WHERE (Pris >= 100) AND (Pris <= 200);

-- Spørring på NULL-merket
-- Ikke hylleplasserte varer
SELECT *
FROM Vare
WHERE Hylle IS NULL;

-- Hylleplasserte varer
SELECT *
FROM Vare
WHERE Hylle IS NOT NULL;










