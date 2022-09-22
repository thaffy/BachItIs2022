from datetime import datetime
import mysql.connector
oblig2021database = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef ', passwd='oblig2021', db='oblig2021')



def registrer_student():
    # 1. Finn høyeste studentnr fra Student-tabellen
        # 1.1 Konverter studentnummer-string til integer, legg til 1
    # 2. Få input fra bruker, men ikke studnr (Kun stringvars)
    # 3. HøyesteStudentnr + 1 blir studentens studnr
    # 4. Oppdater databasen med informasjonen

    # Ingen kontrollsjekk er nødvendig, men kan være greit med duplikatsjekk/verifikasjon på tlf,epost?...
    # hvis man har tid til å lage
    
    print('--')
    print('Registrer Student')

    student_markor = oblig2021database.cursor()

    student_markor.execute('SELECT MAX(Studentnr) AS Storste_studnr FROM Student')

    studnr = []
    studnr += student_markor

    print(studnr[0])
    print(studnr[0][0])
    print('Oppgi følgende informasjon om studenten du vil registrere. ')
    fornavn = input('Fornavn: ')
    etternavn = input('Etternavn: ')
    epost = input('Epost: ')
    telefonnr = int(input('Telefonnr: '))

    storste_studentnr = int(studnr[0][0])
    nytt_studentnr = storste_studentnr + 1

    settinn_student = ('INSERT INTO Student'
                       '(Studentnr,Fornavn,Etternavn,Epost,Telefon)'
                       'VALUES(%s,%s,%s,%s,%s)'
                       )
    nystudent = (nytt_studentnr,fornavn,etternavn,epost,telefonnr)
    student_markor.execute(settinn_student,nystudent)
    oblig2021database.commit()
    student_markor.close()
    # Da funker dette. Noe rotete men grunnidéen er der.
    

def update_student():
    studnr_input = input('Oppgi studentnr: ')

    student_markor = oblig2021database.cursor()

    student_markor.execute('SELECT Studentnr FROM Student')

    studentnrliste = []
    studentnrliste += student_markor

    listelengde = len(studentnrliste)

    funnet = False
    for row in range(listelengde):
        if studnr_input == studentnrliste[row][0]:
            funnet = True

    if funnet == True:
        print('Oppgi ny informasjon: ')
        fornavn = input('Fornavn: ')
        etternavn = input('Etternavn: ')
        epost = input('Epost: ')
        telefonnr = int(input('Telefonnr: '))

        oppdater_student = ("UPDATE Student SET Fornavn = %s, Etternavn = %s, Epost = %s, Telefon = %s WHERE Studentnr = %s")
        student_info = (fornavn,etternavn,epost,telefon,studnr_input)
        student_markor.execute(oppdater_student,student_info)
        oblig2021database.commit()
        
    student_markor.close()


    
    
def registrer_karakter():
    # 1. Få input fra bruker(Studnr,Emnekode,Dato,Karakter)
    # 2. Oppdaterer database - Eksamensresultat-tabellen
    print('--')
    print('Registrer karakter')
    
def planlagte_eksamener():
    # 1. Få input (dato)
    # 2. Skriv ut alle eksamener på gitt dato fra Eksamener-tabellen
    print('--')
    print('Se planlagte eksamener')

    valgt_dato = input('Oppgi dato i YYYYMMDD format: ')

    eksamen_markor = oblig2021database.cursor()

    eksamen_markor.execute('SELECT * FROM Eksamen ORDER BY Dato')

    eksamener = []
    eksamener += eksamen_markor
    for row in eksamener:
        print(row)

    listelengde = len(eksamener)

    print('Emnekode    Dato   Rom')
    for row in range (listelengde):
        if str(valgt_dato) == str(eksamener[row][1]):
            print(eksamener[row][0],eksamener[row][1],eksamener[row][2])

    eksamen_markor.close()
    # Funker, men har ikke IF-test på input-dato
    # Eksamener i en periode er fra-til format. Fra 18/03/2021 til 25/03/2021 f.eks
    
def opprett_eksamen():
    # 1. Få input fra bruker (Emnekode, Dato, Romnr)
    # 2. Kontroller at romnr med dato ikke er i konflikt med andre eksamener
    # 3. Hvis ingen konflikt, oppdater databasen - Eksamen-tabellen
    print('--')
    print('Opprett ny eksamen')

    opprett_markor = oblig2021database.cursor()
    opprett_markor.execute('SELECT * FROM Eksamen')

    eksisterende_eksamener = []
    eksisterende_eksamener += opprett_markor

    print(eksisterende_eksamener)

    
    emnekode = input('Oppgi emnekode: ')
    dato = input('Oppgi dato: ')
    romnr = input('Oppgi romnr: ')

    # Ved bruk av datetime formateres input-datoen til en sammenlignbar dato mot MySQL
    formatert_dato = datetime.strptime(dato, '%Y%m%d').strftime('%Y-%m-%d')
    listelengde = len(eksisterende_eksamener)

    rom_opptatt = False
    for row in range(listelengde):
        if (str(eksisterende_eksamener[row][1]) == str(formatert_dato)) and (eksisterende_eksamener[row][2] == romnr):
            #print('Dette rommet er opptatt på denne dagen.')
            rom_opptatt = True
    if rom_opptatt == True:
        print('Dette rommet er opptatt på denne dagen!')
    else:
        settinn_eksamen = ('INSERT INTO Eksamen'
                           '(Emnekode,Dato,Romnr)'
                           'VALUES(%s,%s,%s)'
                           )
        data_nyeksamen = (emnekode,dato,romnr)
        opprett_markor.execute(settinn_eksamen,data_nyeksamen)
        oblig2021database.commit()

    opprett_markor.close()
            

    
    # print(formatert_dato)

    
    
def eksamensresultat_utskrift():
    # 1. Få input (Studnr)
    # 2. Skriv ut alle eksamensresultat med dato og studiepoeng fra Eksamensresultat-tabellen samt Emne-tabellen
    print('--')
    print('Skriv ut karakterer for student')

    studnr = input('Oppgi studentnr: ')

    

def vitnemål():
    # 1. Få input (Studnr)
    # 2. Hent resten av informasjon (Fornavn, Etternavn, Eksamensresultat, Studiepoeng)
    # 3. Summer studiepoeng
    # 4. Skriv ut alle resultater, med sum studiepoeng fra Student-tabellen, Eksamensresultat-tabellen, Emne-tabellen
    print('--')
    print('Skriv ut vitnemål')



def slett_student():
    print('--')

    studnr = input('Oppgi studentnr: ')
    
        
                            




def main():

    fortsette = True

    while fortsette:
        print()
        print('-- Hovedmeny --')
        print('Oblig 2021')
        print('-')
        print('1. Registrer Student')
        print('2. Registrer Karakter')
        print('3. Se planlagte eksamener')
        print('4. Opprett en eksamen')
        print('5. Karakterutskrift')
        print('6. Vitnemålutskrift')
        print('7. Oppdater student')
        print('8. Slett student')

        svar = input('Hva vil du gjøre? ')

        if svar == '1':
            registrer_student()
        elif svar == '2':
            registrer_karakter()
        elif svar == '3':
            planlagte_eksamener()
        elif svar == '4':
            opprett_eksamen()
        elif svar == '5':
            eksamensresultat_utskrift()
        elif svar == '6':
            vitnemål()
        elif svar == '7':
            update_student()
        elif svar == '8':
            slett_student()
        else:
            print('Program avsluttet!')
            fortsette = False

            oblig2021database.close()


main()


    



