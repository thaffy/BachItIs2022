import os

def slettstudent():
    # Delprogram for å slette studenter.
    print('------------------------------')
    print('Valg 2 - Slett eksisterende student.')
    print('-')

    slettstudent_fortsette = True

    while slettstudent_fortsette == True:

        finnes = False

        studentnr_input = input('Skriv inn studentnr: ')

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

            if studentnr_input == studnr:
                finnes = True
                
            studnr=student_fil.readline()

        if finnes == True:
            student_fil.close()

            har_resultat = False

            eksamen_fil = open('eksamensresultat.txt','r')

            emnekode = eksamen_fil.readline()

            while emnekode != '':
                studnr = eksamen_fil.readline()
                karakter = eksamen_fil.readline()

                emnekode = emnekode.rstrip('\n')
                studnr = studnr.rstrip('\n')
                karakter = karakter.rstrip('\n')

                if studentnr_input == studnr:
                    har_resultat = True

                emnekode = eksamen_fil.readline()
                
            # Hvis studenten eksisterer, men har eksamensresultat.
            if har_resultat == True:
                eksamen_fil.close()
                print('------------------------------')
                print('Du oppga studentnr',studentnr_input,'.')
                print('Denne studenten kan ikke slettes. Studenten har eksamensresultat.')
                print('------------------------------')
                
            # Hvis studenten eksisterer og har ikke eksamensresultat regisrert.
            else:
                eksamen_fil.close()

                # Åpner student.txt i read modus, og oppretter temp.txt i write modus.
                student_fil = open('student.txt','r')
                temp_fil = open('temp.txt','w')

                funnet = False
                
                studnr = student_fil.readline()

                while studnr != '':
                    fornavn = student_fil.readline()
                    etternavn = student_fil.readline()
                    studerer = student_fil.readline()

                    studnr = studnr.rstrip('\n')
                    fornavn = fornavn.rstrip('\n')
                    etternavn = etternavn.rstrip('\n')
                    studerer = studerer.rstrip('\n')

                    if studnr != studentnr_input:
                        temp_fil.write(studnr + '\n')
                        temp_fil.write(fornavn + '\n')
                        temp_fil.write(etternavn + '\n')
                        temp_fil.write(studerer + '\n')
                    else:
                        funnet = True

                    studnr = student_fil.readline()

                # Lukker filene student.txt og temp.txt
                student_fil.close()
                temp_fil.close()

                # Sletter student.txt og erstatter den med temp.txt
                os.remove('student.txt')
                os.rename('temp.txt','student.txt')

                print('------------------------------')
                print('Du oppga studentnr',studentnr_input,'.')
                print('Denne studenten har blitt slettet.')
                print('------------------------------')
                
        # Hvis studenten ikke er registrert i student.txt
        else:
            print('------------------------------')
            print('Du oppga studentnr',studentnr_input,'.')
            print('Denne studenten eksisterer ikke i systemet.')
            print('------------------------------')
            student_fil.close()

        # Spør om bruker vil legge til flere studenter.
        svar = input('Vil du slette en annen student? j/n: ')
        
        if svar == 'n' or svar == 'N' or svar == 'nei' or svar == 'Nei' or svar == 'NEI':
            slettstudent_fortsette = False

slettstudent()
