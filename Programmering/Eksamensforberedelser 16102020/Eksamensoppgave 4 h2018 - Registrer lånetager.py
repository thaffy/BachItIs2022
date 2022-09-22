# Bok, for hver bok lagres <isbn, tittel, forfattere(e), forlag, utgitt_aar>

# Laaner, for hver lånetager lagres <lnr, fornavn, etternavn, mobilnr>

# Utlaan, for hvert utlån lagres <utlaansnr, lnr, isbn, utlaansdato, innleveringsdato>

def registrer_lanetager():
    # Delprogram for å registrere lånetager

    print('-----')
    print(' Valg 1 - Registrer lånetager.')
    print('-')

    fortsette = True

    while fortsette == True:

        duplikat = False

        input_mobilnr = input('Skriv inn lånetagers mobilnr: ')

        lanetager_fil = open('Laaner.txt','r')

        lnr = lanetager_fil.readline()

        while lnr != '':
            fornavn = lanetager_fil.readline()
            etternavn = lanetager_fil.readline()
            mobilnr = lanetager_fil.readline()

            lnr = lnr.rstrip('\n')
            fornavn = fornavn.rstrip('\n')
            etternavn = etternavn.rstrip('\n')
            mobilnr = mobilnr.rstrip('\n')

            if input_mobilnr == mobilnr:
                duplikat = True

            lnr = lanetager_fil.readline()

        if duplikat == True:
            print('-----')
            print('Du oppga mobilnummeret',input_mobilnr)
            print('Denne lånetageren er i systemet fra før og kan ikke lagres på nytt.')
            print('-----')
            lanetager_fil.close()
        else:
            lanetager_fil.close()

            lanetager_fil = open('Laaner.txt','a')

            lnr_input = input('Skriv inn lånetager-nummer: ')
            fornavn_input = input('Skriv inn fornavn: ')
            etternavn_input = input('Skriv inn etternavn: ')

            lanetager_fil.write(lnr_input + '\n')
            lanetager_fil.write(fornavn_input + '\n')
            lanetager_fil.write(etternavn_input + '\n')
            lanetager_fil.write(input_mobilnr + '\n')

        lanetager_fil.close()

        svar = input('Vil du legge til en ny lånetager? j/n: ')

        if svar == 'n' or svar == 'N' or svar == 'nei' or svar == 'Nei' or svar == 'NEI':
            fortsette = False
            
            

        
    


registrer_lanetager()
