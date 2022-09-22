-- Oppgave 1 kapittel 2
USE oppgave1kap2;

-- 2.8 a)
SELECT *
From Film
WHERE År = 1988;

-- 2.8 b)
SELECT Tittel
From Film
WHERE (ÅR >= 1980) AND (År < 1990);

-- 2.8 c)
SELECT *
FROM Film
WHERE (Alder < 10) AND (Tid < 130) AND (UPPER(Sjanger) = 'Komedie');

-- 2.8 d)
SELECT Tittel
FROM Film
WHERE (UPPER(Sjanger) = 'Action') OR (UPPER(Sjanger) = 'Western');

-- 2.8 e)
SELECT DISTINCT Land
FROM Film
ORDER BY Land ;

-- 2.8 i)
SELECT *
FROM Film
WHERE (UPPER(Tittel) LIKE '%NOW');