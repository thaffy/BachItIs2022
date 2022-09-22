# Delprogram for å skrive ut karakter til en gitt student
print('------------------------------')
print('Valg 3 - Karakterutskrift')
print('-')


funnet = False

studentnr_input = input('Skriv inn studentnummer: ')

student_fil = open('student.txt','r')

studnr = student_fil.readline()

while studnr != '':
    # Leser andre, tredje og fjerde linje
    fornavn = student_fil.readline()
    etternavn = student_fil.readline()
    studerer = student_fil.readline()

    # Fjerner linjeskift \n
    studnr = studnr.rstrip('\n')
    fornavn = fornavn.rstrip('\n')
    etternavn = etternavn.rstrip('\n')
    studerer = studerer.rstrip('\n')

    if studnr == studentnr_input:
        funnet = True
        print('------------------------------')
        print('Studentnummer:',studnr)
        print(fornavn,etternavn,'-', studerer)
        print()

        

    studnr = student_fil.readline()
    
if funnet == False:
    print('------------------------------')
    print('Du oppga studentnummer',studentnr_input,'.')
    print('Denne studenten eksisterer ikke i systemet.')
    print('------------------------------')
    student_fil.close()
    

else:

    # Vi trenger ikke student.txt lenger, så den lukkes.
    student_fil.close()

    # Åpner eksamenresultat.txt for å sjekke om studenten har resultater, og evt hvilke disse er.
    eksamen_fil = open('eksamensresultat.txt','r')

    har_resultat = False

    emnekode = eksamen_fil.readline()

    while emnekode != '':
        studnr = eksamen_fil.readline()
        karakter = eksamen_fil.readline()

        emnekode = emnekode.rstrip('\n')
        studnr = studnr.rstrip('\n')
        karakter = karakter.rstrip('\n')

        if studentnr_input == studnr:
            har_resultat = True

            emnenavn_fil = open('emne.txt','r')

            emnenavn_fil_emnekode = emnenavn_fil.readline()

            while emnenavn_fil_emnekode != '':
                
                emnenavn_fil_emnenavn = emnenavn_fil.readline()

                emnenavn_fil_emnekode = emnenavn_fil_emnekode.rstrip('\n')
                emnenavn_fil_emnenavn = emnenavn_fil_emnenavn.rstrip('\n')
                
                if emnenavn_fil_emnekode == emnekode:
                    emnenavn = emnenavn_fil_emnenavn
                    
                emnenavn_fil_emnekode = emnenavn_fil.readline()
                
        
                

            print(emnekode,emnenavn,'- Karakter:',karakter)
            emnenavn_fil.close()

            
        emnekode = eksamen_fil.readline()

    if har_resultat == True:
        
        print('------------------------------')
    else:
        print('Ingen resultat registrert.')
        print('------------------------------')

    eksamen_fil.close()
                       






