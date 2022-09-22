USE oblig2021;

SELECT *
FROM Eksamen;


INSERT INTO Student VALUES
('240229','Markus','Hamre','markushamre@hotmail.com','97749465'),
('250250','Fredrik','Hamre','fredrikhamre@hotmail.com','98746465'),
('260260','Kari','Vilikke','Karivilikkelevere@gmail.com','99969666'),
('270270','Ståle','Vikhagen','manofsteel@usn.no','98765432');

INSERT INTO Emne VALUES
('PRG1000','Grunnleggende Programmering 1','7.5'),
('PRG1100','Grunnleggende Programmering 2','7.5'),
('INF1000','Informasjonsysstemer','7.5'),
('SYS1000','Systemutvikling','7.5'),
('ORL1000','Organisering og Ledelse','7.5'),
('PRO1000','Praktisk Prosjektarbeid','7.5'),
('DAT1000','Database 1','7.5'),
('DAT1100','Database 2','7.5');

INSERT INTO Rom VALUES
('E209','50'),
('E210','45'),
('E208','65'),
('B108','10');

INSERT INTO Eksamen VALUES
('PRG1000','20201202','E209'),
('PRG1100','20210503','E208');

INSERT INTO Eksamensresultat VALUES
('240229','PRG1000','20201202','A');



