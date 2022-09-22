DROP SCHEMA IF EXISTS Studieadm;
-- Oppretter databasen
DROP SCHEMA IF EXISTS Studieadm;
CREATE SCHEMA IF NOT EXISTS Studieadm;

USE Studieadm;

-- Oppretter tabellen Student
CREATE TABLE Student
(
Studentnr INTEGER(6) PRIMARY KEY,
Fornavn VARCHAR(30) NOT NULL,
Etternavn VARCHAR(30) NOT NULL,
Epost VARCHAR(30) UNIQUE,
Fødselsdato DATE,
Kjønn CHAR(6)
);

INSERT INTO Student VALUES ('240229','Markus','Hamre','markushamre@hotmail.com','1995-09-12','Mann');
INSERT INTO Student VALUES ('240240','Heidi','Blåkossen','heideblaakossen@gmail.com','1993-02-01','Kvinne');

INSERT INTO Student VALUES ('240250','Thomas','Riksfjord','thomas@riksfjord.com','1996-08-26','Mann');
INSERT INTO Student VALUES ('250100','Nils','Hansen','nilshansen95@hotmail.com','1998-12-12','Mann');

INSERT INTO Student VALUES ('250200','Sigrid','Smeplass','sigridsmeplass@gmail.com','1995-03-09','Kvinne');
INSERT INTO Student VALUES ('250300','Tonje','Aaberge','tonjeaaberge@gmail.com','1991-04-03','Kvinne');

INSERT INTO Student VALUES ('250400','Lars','Kåborg','larskaaborg@hotmail.com','1995-05-17','Mann');
INSERT INTO Student VALUES ('260362','Anders','Jacobsen','anderjacobsen123@hotmail.com','1997-05-19','Mann');

INSERT INTO Student VALUES ('260800','Leah','Thomassen','leahthomassen@hotmail.com','1996-03-26','Kvinne');
INSERT INTO Student VALUES ('260801','Ingrid','Thomassen','ingridthomassen@hotmail.com','1996-03-26','Kvinne');

SELECT *
FROM Student;


