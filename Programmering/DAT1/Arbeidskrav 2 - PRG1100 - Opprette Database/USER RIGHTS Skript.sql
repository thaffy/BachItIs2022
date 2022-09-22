USE oblig2021;

CREATE USER 'Eksamenssjef' IDENTIFIED BY 'oblig2021';


GRANT SELECT ON Eksamen TO 'Eksamenssjef';
GRANT INSERT ON Eksamen TO 'Eksamenssjef';
GRANT UPDATE ON Eksamen TO 'Eksamenssjef';
GRANT DELETE ON Eksamen TO 'Eksamenssjef';

GRANT INSERT ON Student TO 'Eksamenssjef';
GRANT SELECT ON Student TO 'Eksamenssjef';
GRANT UPDATE ON Student TO 'Eksamenssjef';
GRANT DELETE ON Student TO 'Eksamenssjef';

GRANT SELECT ON Emne TO 'Eksamenssjef';

GRANT SELECT ON Eksamensresultat TO 'Eksamenssjef';
GRANT INSERT ON Eksamensresultat TO 'Eksamenssjef';
GRANT UPDATE ON Eksamensresultat TO 'Eksamenssjef';
GRANT DELETE ON Eksamensresultat TO 'Eksamenssjef';
