# Obligatorisk Arbeidskrav 2 - Markus Hamre
import os

def leggtilstudent():
    # Delprogram for å legge til nye studenter i student.txt
    print('------------------------------')
    print('Valg 1 - Legg til student.')
    print('-')

    leggtilstudent_fortsette = True
    
    while leggtilstudent_fortsette == True:
        
        # Bolsk variabel som brukes til duplikat-sjekk
        duplikat = False

        studentnr_input = input('Skriv inn studentnummer: ')

        student_fil = open('student.txt','r')

        # Leser første linje i student.txt
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
                duplikat = True
                
            studnr=student_fil.readline()

        if duplikat == True:
            print('------------------------------')
            print('Du oppga studentnummer',studentnr_input,'-')
            print('Denne studenten eksisterer allerede i systemet.')
            print('------------------------------')
            student_fil.close()
        else:
            # Lukker student.txt som var i read-modus.
            student_fil.close()

            # Åpner student.txt i append modus.
            student_fil = open('student.txt','a')

            # Spør om resten av informasjonen om studenten først etter at duplikat-sjekk er gjort
            fornavn_input = input('Skriv inn fornavn: ')
            etternavn_input = input('Skriv inn etternavn: ')
            studie_input = input('Skriv inn studie: ')

            # Legger til input fra bruker i student.txt
            student_fil.write(studentnr_input + '\n')
            student_fil.write(fornavn_input + '\n')
            student_fil.write(etternavn_input + '\n')
            student_fil.write(studie_input + '\n')
            

        student_fil.close()
        
        # Spør om bruker vil legge til flere studenter.
        svar = input('Vil du legge til en ny student? j/n: ')
        
        if svar == 'n' or svar == 'N' or svar == 'nei' or svar == 'Nei' or svar == 'NEI':
            leggtilstudent_fortsette = False



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

            # Åpner eksamensresultat.txt for å sjekke om studenten har resultat, og da om studenten kan/kan ikke slettes.
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



def karakterutskrift():
    # Delprogram for å skrive ut karakter til en gitt student
    print('------------------------------')
    print('Valg 3 - Karakterutskrift')
    print('-')

    karakterutskrift_fortsette = True

    while karakterutskrift_fortsette == True:

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

                # Hvis studenten har resultat
                if studentnr_input == studnr:
                    har_resultat = True

                    # Åpner emne.txt for å hente emnebeskrivelse
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

            # Spør om bruker vil skrive ut flere karakterutskrifter
            svar = input('Vil du gjøre flere karakterutskrifter? j/n: ')
            
            if svar == 'n' or svar == 'N' or svar == 'nei' or svar == 'Nei' or svar == 'NEI':
                karakterutskrift_fortsette = False
    

def main():
    # Hovedmeny og returpunkt etter at hvert delprogram har blitt kjørt.

    # Bolsk variabel for å avslutte while-løkka når bruker bestemmer det.
    fortsette = True

    # Hovedmeny for programvalg. Etter hvert delprogram ender man opp her igjen.
    while fortsette == True:
        print('------------------------------')
        print('- Meny')
        print('- ')
        print('- Valg 1 - Legg til student')
        print('- Valg 2 - Slett en student')
        print('- Valg 3 - Karakterutskrift')
        print('- ')
        print('- Valg 0 - Avslutt programmet')
        print('------------------------------')
        
        valgt_program = int(input('Hva vil du gjøre? '))

        # If-testene sender bruker til riktig delprogram, eller avslutter programmet, basert på hva brukeren svarer.
        if valgt_program == 1:
            leggtilstudent()
        else:
            if valgt_program == 2:
                slettstudent()
            else:
                if valgt_program == 3:
                    karakterutskrift()
                else:
                    # Når bruker svarer 0 avsluttes while-løkka og programmet avsluttes.
                    if valgt_program == 0:
                        fortsette = False
                        print()
                        print('Programet er avsluttet! ')
                        
                    # Hvis bruker ikke har oppgitt en gyldig verdi spør programmet om ny input.
                    # Dette hindrer programmet fra å avslutte hvis man skriver inn ugyldig tall med uhell.
                    else:
                        print('Tallet du skrev inn er ugyldig.')
                        print('Vennligst velg ved bruk av tallene 1, 2, 3 eller 0.')
                        

            
# Her kjøres main - Menyen som brukeren ser på programstart, og etter at hvert delprogram er ferdig
main()
