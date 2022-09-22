# Innsetting av data i database fra Python
# Innsetting ved verdiene "rett i cursoren"

import mysql.connector

#1. Koble mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,user='Lagersjefen2021',passwd='lagerpw',db='heltnydatabase')

#2. Opprette cursoren/markøren
settinn_markor=mindatabase.cursor()

markor=mindatabase.cursor()


#3. Bruke databsen
settinn_markor.execute("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES('9999','Testvare',99.99,999,99,'T99')"
                       )

# Bruk commit når man skal bekrefte at jobben er ferdig
mindatabase.commit()

settinn_markor.execute("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES('8888','EndaenTestvare',88.88,888,88,'T88')"
                       )
mindatabase.commit()
#4. Bruke resultatet
markor.execute('SELECT * FROM Vare')
for row in markor:
    print(row)

#5. Koble ned
settinn_markor.close()
markor.close()
mindatabase.close()
