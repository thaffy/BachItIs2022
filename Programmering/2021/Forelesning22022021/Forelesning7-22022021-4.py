# Innsetting av data i database fra Python
# Innsetting ved verdiene inn i variable som referes i cursoren

import mysql.connector

#1. Koble mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,user='Lagersjefen2021',passwd='lagerpw',db='heltnydatabase')

#2. Opprette cursoren/markøren
settinn_markor=mindatabase.cursor()

markor=mindatabase.cursor()


#3. Bruke databsen
varenr = input('Oppgi varnr: ')
varenavn = input('Oppgi varenavn: ')
pris = float(input('Oppgi pris: '))
katnr = int(input('Oppgi katnr: '))
antall = int(input('Oppgi antall: '))
hylle = input('Oppgi hylleplassering: ')

settinn_vare = ("INSERT INTO Vare"
                "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                "VALUES(%s,%s,%s,%s,%s,%s)"
                )
datany_vare = (varenr,varenavn,pris,katnr,antall,hylle)
settinn_markor.execute(settinn_vare,datany_vare)

mindatabase.commit()
#4. Bruke resultatet
markor.execute('SELECT * FROM Vare')
for row in markor:
    print(row)

#5. Koble ned
settinn_markor.close()
markor.close()
mindatabase.close()
