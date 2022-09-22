-- Script for å sette data inn i ansattpersonal2021
-- Her er dataene satt inn i riktig rekkefølge med tanke på primær og fremmednøkler.

USE ansattpersonal2021;

INSERT INTO Avdeling VALUES ('1000','IT');
INSERT INTO Avdeling VALUES ('2000','Administrasjon');
INSERT INTO Avdeling VALUES ('3000','Økonomi');
INSERT INTO Avdeling VALUES ('4000','Personal');
INSERT INTO Avdeling VALUES ('5000','Vedlikehold');


INSERT INTO Stillingstype VALUES ('1000','Avdelingssjef');
INSERT INTO Stillingstype VALUES ('2000','Konsulent');
INSERT INTO Stillingstype VALUES ('3000','Økonomimedarbeider');
INSERT INTO Stillingstype VALUES ('4000','Sekretær');
INSERT INTO Stillingstype VALUES ('5000','Trainee');


INSERT INTO Postkatalog VALUES ('1000','Oslo');
INSERT INTO Postkatalog VALUES ('1500','Molde');
INSERT INTO Postkatalog VALUES ('2000','Tromsø');
INSERT INTO Postkatalog VALUES ('2500','Bodø');
INSERT INTO Postkatalog VALUES ('3000','Hønefoss');
INSERT INTO Postkatalog VALUES ('3500','Buskerud');


INSERT INTO Kurs VALUES ('1000','HMS');
INSERT INTO Kurs VALUES ('2000','Brannvakt');
INSERT INTO Kurs VALUES ('3000','Førstehjelp');
INSERT INTO Kurs VALUES ('4000','Sistehjelp');


INSERT INTO Ansatt VALUES ('1000','Markus','Hamre','Osloveien 3','97749465','1000','3000','3500');
INSERT INTO Ansatt VALUES ('2000','Kari','Vilikke','Strandgata 4','98745634','3000','3000','3000');
INSERT INTO Ansatt VALUES ('3000','Håkon','Ormstad','Lierlia 10','93412345','2000','2000','3000');
INSERT INTO Ansatt VALUES ('4000','Terje','Blomstervik','Terjesvei 2','98756456','1000','1000','1000');
INSERT INTO Ansatt VALUES ('5000','Sigrid','Heisannsbom','Grusstien 8','98769454','2000','4000','2000');

-- dato er skrevet som år-måned-dag
-- etter CONSTRAINT i opprettelses-scriptet må vurderings-feltet (satt som NULL her) være en av Besått/Ikke bestått/Gjennomført/Ikke møtt. Men har brukt NULL fordi lat
INSERT INTO Kursdeltagelse VALUES ('1000','1000','2012-01-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('1000','2000','2012-02-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('2000','1000','2012-02-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('2000','2000','2012-03-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('3000','3000','2012-03-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('4000','2000','2012-03-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('5000','2000','2012-04-02',NULL);
INSERT INTO Kursdeltagelse VALUES ('5000','3000','2012-04-02',NULL);



