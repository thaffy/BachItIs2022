-- Introduksjon DDL, opprette database, opprette tabell, legge inn data

-- Sletter databasen hvis den finnes fra før !! RISKY !!
DROP SCHEMA IF EXISTS heltnydatabase;
-- Oppretter databasen
CREATE SCHEMA IF NOT EXISTS heltnydatabase;

USE heltnydatabase;

-- Oppretter tabellen Vare
CREATE TABLE Vare
(
VNr CHAR(5) PRIMARY KEY,
Betegnelse VARCHAR(30),
Pris DECIMAL(8,2),
KatNr SMALLINT,
Antall INTEGER,
Hylle CHAR(3)
);

-- Legge inn data i tabellen vare, vare nr 1
INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES('90693','Marsipantang','57.00','4','0','B17');

-- her legger dere inn vare nr 2
INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('44939','Hobbymaling, 6 farger','115.00','2','2','B02');

-- vare nr 3
INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('10830','Nisseskjegg, 30 cm','57.50','13','42',NULL);

-- her legger dere inn vare nr 4 tom 8 med samme struktur som over

INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('33044','Blandet blomsterfrø','14.50','15','1080','E05');

INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('15217','Kram tørrfluekorker, 5stk','32.00','7','213','B42');

INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('90164','Lakrisekstrakt, 100g','75.50','4','104','B06');

INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('15207','Antron garn, hvit','24.50','7','21','B41');

INSERT INTO Vare(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('13001','Glasskuler, 100gr','38.00','13','0','E11');

-- vare nr 9
-- Trenger ikke feltnavnlista hvis data i alle felt
INSERT INTO Vare VALUES ('21032','Furuspon 3cm','57.50','17','240','B32');

-- Her legger dere vare 10 tom 15 i kortform

INSERT INTO Vare VALUES ('33045','Blomkarse','17.50','15','1206','E05');
INSERT INTO Vare VALUES ('55130','Moro med marsipan','298.50','10','140','C20');
INSERT INTO Vare VALUES ('15211','Tubeflue verktøy','209.00','7','39','B49');
INSERT INTO Vare VALUES ('42615','Gipsform marihøner','106.00','3','124','B03');
INSERT INTO Vare VALUES ('64551','Hengebogonia, 10stk.','118.00','16','206',NULL);
INSERT INTO Vare VALUES ('65247','Liten plantespade','75.00','1','76','A25');



SELECT *
FROM Vare;