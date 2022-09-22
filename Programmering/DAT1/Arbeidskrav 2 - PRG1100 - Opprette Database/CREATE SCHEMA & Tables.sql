DROP SCHEMA IF EXISTS oblig2021;
CREATE SCHEMA oblig2021;

USE oblig2021;

CREATE TABLE Student
(
Studentnr CHAR(6),
Fornavn CHAR(30) NOT NULL,
Etternavn CHAR(20) NOT NULL,
Epost CHAR(40),
Telefon CHAR(8),
CONSTRAINT StudentPK PRIMARY KEY(Studentnr)
);

CREATE TABLE Emne
(
Emnekode CHAR(8),
Emnenavn CHAR(40) NOT NULL,
Studiepoeng DECIMAL(3,1) NOT NULL,
CONSTRAINT EmnePK PRIMARY KEY(Emnekode)
);

CREATE TABLE Rom
(
Romnr CHAR(4),
Antallplasser INTEGER(3) NOT NULL,
CONSTRAINT RomPK PRIMARY KEY(Romnr)
);

CREATE TABLE Eksamen
(
Emnekode CHAR(8),
Dato DATE,
Romnr CHAR(4),
CONSTRAINT EksamenPK PRIMARY KEY(Emnekode,Dato,Romnr),
CONSTRAINT EksamenEmneFK FOREIGN KEY(Emnekode) REFERENCES Emne(Emnekode),
CONSTRAINT EksamenRomFK FOREIGN KEY(Romnr) REFERENCES Rom(Romnr)
);

CREATE TABLE Eksamensresultat
(
Studentnr CHAR(6),
Emnekode CHAR(8),
Dato DATE,
Karakter CHAR(1),
CONSTRAINT EksamensresultatPK PRIMARY KEY(Studentnr,Emnekode,Dato),
CONSTRAINT EksamensresulstatStudentFK FOREIGN KEY(Studentnr) REFERENCES Student(Studentnr),
CONSTRAINT EksamensresultatEksamenFK FOREIGN KEY(Emnekode,Dato) REFERENCES Eksamen(Emnekode,Dato)
);

SELECT *
FROM Student;

SELECT *,DATE_FORMAT(dato, '%Y%m%d') AS FormatertDato
FROM Eksamen;

