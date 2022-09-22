USE heltnydatabase;
-- tabellen blir sortert på primærnøkkelen

SELECT *
FROM Vare;

-- primærnøkkelen holder orden på dubletter, ikke mulig å registrere to varer på samme VNr

INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle)
VALUES ('65247','Stor plantespade','175.00','1','103','A26');