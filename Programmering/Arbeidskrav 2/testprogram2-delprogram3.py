


# Boolsk variabel som brukes til søk etter at studentnr er skrevet inn.
funnet = False

# Bruker blir først bedt om bare studentnr - Hvis studentnummeret allerede finnes i student.txt trengs ikke resten av informasjonen enda.
studnr = input('Skriv inn studentnr: ')

# Åpner student.txt i read-modus for å starte søk
student_fil = open('student.txt','r')


les_linje = student_fil.readline()

while les_linje != '':
    fornavn = student_fil.readline()

    les_linje = les_linje.rstrip('\n')

    if les_linje == studnr:
        funnet = True
        # print('-----')
        # print(les_linje)
        studentnummer=les_linje
        
        fornavn = fornavn.rstrip('\n')
        # print(fornavn)

        les_linje = student_fil.readline()
        etternavn = les_linje.rstrip('\n')
        # print(etternavn)

        les_linje = student_fil.readline()
        studerer = les_linje.rstrip('\n')
        # print(studerer)
        # print('-----')

        student_fil.close

        eksamensresultat = open('eksamensresultat.txt','r')

        funnet_karakter = False

        les_karakter = eksamensresultat.readline()
        print(les_karakter)

        while les_karakter != '':
            les_karakter = eksamensresultat.readline()
            les_karakter = les_karakter.rstrip('\n')
            

            if les_karakter == studnr:
                funnet_karakter = True
                emnekode = eksamensresultat.readline()
                print(emnekode)
                print(les_karakter)
                
        

        print('------------------------------')
        print(fornavn, etternavn,'  ',studerer)

    les_linje = student_fil.readline()

if funnet == False:
    print('------------------------------')
    print('Denne studenten eksisterer ikke i systemet.')
    print('------------------------------')
    student_fil.close()







        


student_fil.close()
            

            
