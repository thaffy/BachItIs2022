# Obligatorisk Arbeidskrav 2 - Markus Hamre

def leggtilstudent():
    # Delprogram for å legge til nye studenter i student.txt
    print('------------------------------')
    print('Valg 1 - Legg til student.')
    print('-')

    # While-løkke med boolsk variabel for restart av delprogrammet
    leggtilstudent_fortsette = True
    while leggtilstudent_fortsette == True:

        # Boolsk variabel som brukes til søk etter at studentnr er skrevet inn.
        duplikat = False

        # Bruker blir først bedt om bare studentnr - Hvis studentnummeret allerede finnes i student.txt trengs ikke resten av informasjonen enda.
        studnr = input('Skriv inn studentnr: ')

        # Åpner student.txt i read-modus for å starte søk
        student_fil = open('student.txt','r')


        les_linje = student_fil.readline()

        while les_linje != '':
            fornavn = student_fil.readline()

            les_linje = les_linje.rstrip('\n')

            if les_linje == studnr:
                duplikat = True

                
            les_linje = student_fil.readline()

        # Hvis studentnummeret finnes fra før i student.txt får brukeren beskjed om at studenten allerede er skrevet inn.
        # Brukeren blir deretter sendt til spørsmål om programmet skal starte på nytt eller ikke.
        if duplikat == True:
            print('------------------------------')
            print('Du oppga studentnummer',studnr,'.')
            print('Denne studenten eksisterer allerede i systemet.')
            print('------------------------------')
            student_fil.close()
            
        # Hvis studentnummeret ikke finnes fra før blir bruker bedt om å skrive inn resten av opplysningene som skal i student.txt
        else:

            # student.txt må lukkes og åpnes på nytt ettersom den var i read-modus til nå.
            student_fil.close()

            # Åpner student.txt i append-modus for å legge til input fra bruker.
            student_fil = open('student.txt','a')

            fornavn = input('Skriv inn fornavn: ')
            etternavn = input('Skriv inn etternavn: ')
            studie = input('Skriv inn studiue: ')
            
            # Inputen fra brukeren skrives inn i student.txt
            student_fil.write(studnr + '\n')
            student_fil.write(fornavn + '\n')
            student_fil.write(etternavn + '\n')
            student_fil.write(studie + '\n')

        student_fil.close()
        # Spør om bruker vil legge til flere studenter.
        svar = input('Vil du legge til en ny student? j/n: ')
        if svar == 'n' or svar == 'N' or svar == 'nei' or svar == 'Nei' or svar == 'NEI':
            leggtilstudent_fortsette = False



def slettstudent():
    # Delprogram for å slette studenter.
    print('------------------------------')
    print('Valg 2 - Slett eksisterende studenter')
    print('-')

def karakterutskrift():
    # Delprogram for å skrive ut karakter til en gitt student
    print('------------------------------')
    print('Valg 3 - Karakterutskrift')
    print('-')
    









def main():
    # Hovedmeny og returpunkt etter at hvert delprogram har blitt kjørt.

    # Boolsk variabel for å avslutte while-løkka når bruker bestemmer det.
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
                        print('Vennligst velg ved bruk av tallene 1, 2, 3 eller 0.')
                        

            
# Her kjøres main - Menyen som brukeren ser på programstart, og etter at hvert delprogram er ferdig
main()
