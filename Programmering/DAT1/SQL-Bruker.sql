USE heltnydatabase;

SELECT *
FROM Vare;

CREATE USER 'Lagersjefen2021' IDENTIFIED BY 'lagerpw';

GRANT SELECT ON Vare TO 'Lagersjefen2021';

GRANT INSERT ON Vare TO 'Lagersjefen2021';
