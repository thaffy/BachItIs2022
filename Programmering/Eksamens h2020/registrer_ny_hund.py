def registrer_ny_hund():
    # Delprogram for å registrere ny hund

    fortsette = True

    while fortsette == True:

        duplikat = False

        # Spør om hundenr for sjekk
        input_hunde_id = input('Skriv inn HundeID: ')

        # Åpner hund.txt i read-modus og leser første linje 
        hund_fil = open('hund.txt','r')
        hunde_id = hund_fil.readline()

        while hunde_id != '':

            # Leser 2 til og med 6 linje
            oppdretter_id = hund_fil.readline()
            hunde_eier_id = hund_fil.readline()
            hund_navn = hund_fil.readline()
            kjonn = hund_fil.readline()
            fodt = hund_fil.readline()

            # Fjerner linjeskift \n

            hunde_id = hunde_id.rstrip('\n')
            oppdretter_id = oppdretter_id.rstrip('\n')
            hunde_eier_id = hunde_eier_id.rstrip('\n')
            hund_navn = hund_navn.rstrip('\n')
            kjonn = kjonn.rstrip('\n')
            fodt = fodt.rstrip('\n')

            if input_hunde_id == hunde_id:
                duplikat = True

            hunde_id = hund_fil.readline()

        # Hva som skjer hvis hunden er lagret fra før
        if duplikat == True:
            print('-----')
            print('Du oppga HundeIDen',input_hunde_id,)
            print('Denne hunden er registrert i systemet fra før og kan ikke lagres på nytt.')
            print('-----')
            hund_fil.close()

        # Hva som skjer hvis hunden ikke er lagret fra før
        else:
            hund_fil.close()

            # Spør om oppretter ID for sjekk
            input_oppdretter_id = input('Oppgi oppretter ID: ')

            oppdretter_eksisterer = False

            # Åpner oppdretter.txt
            oppdretter_fil = open('oppdretter.txt', 'r')

            oppdretter_fil_id = oppdretter_fil.readline()

            while oppdretter_fil_id != '':

                kennelnavn = oppdretter_fil.readline()
                kenneleier_fornavn = oppdretter_fil.readline()
                kenneleier_etternavn = oppdretter_fil.readline()

                # Fjerner linjeskift \n

                oppdretter_fil_id = oppdretter_fil_id.rstrip('\n')
                kennelnavn = kennelnavn.rstrip('\n')
                kenneleier_fornavn = kenneleier_fornavn.rstrip('\n')
                kenneleier_etternavn = kenneleier_etternavn.rstrip('\n')

                if input_oppdretter_id == oppdretter_fil_id:

                    eksisterer = True

                oppdretter_fil_id = oppdretter_fil.readline()

            # Hva som skjer hvis oppdretter eksisterer 
            if eksisterer == True:
                
                oppdretter_fil.close()

                eier_eksisterer = False

                input_hunde_eier_id = input('Oppgi Hundeeier ID: ')
                hundeeier_fil = open('hundeeier.txt','r')
                
                hundeeier_fil_id = hundeeier_fil.readline()

                while hundeeier_fil_id != '':
                    hundeeier_fornavn = hundeeier_fil.readline()
                    hundeeier_etternavn = hundeeier_fil.readline()

                    hundeeier_fil_id = hundeeier_fil_id.rstrip('\n')
                    hundeeier_fornavn = hundeeier_fornavn.rstrip('\n')
                    hundeeier_etternavn = hundeeier_etternavn.rstrip('\n')

                    if input_hunde_eier_id == hundeeier_fil_id:

                        eier_eksisterer = True

                    hundeeier_fil_id = hundeeier_fil.readline()


                # Hva som skjer hvis hunden ikke er lagret fra før, og eier + oppdretter eksisterer
                if eier_eksisterer == True:

                    hundeeier_fil.close()

                    # Spør om resten av informasjonen om hunden.
                    input_hund_navn = input('Oppgi hundens navn: ')
                    input_kjonn = input('Oppgi hundens kjønn: ')
                    input_fodt = input('Oppgi hundens fødelsdato: ')

                    hund_fil = open('hund.txt','a')

                    # Skriver inn informasjonen i hund.txt
                    hund_fil.write(input_hunde_id + '\n')
                    hund_fil.write(input_oppdretter_id + '\n')
                    hund_fil.write(input_hunde_eier_id + '\n')
                    hund_fil.write(input_hund_navn + '\n')
                    hund_fil.write(input_kjonn + '\n')
                    hund_fil.write(input_fodt + '\n')

                    hundeeier_fil.close()
                                

                    
                # Hva som skjer hvis HundeEier ikke eksisterer i systemet
                else:
                    hundeeier_fil.close()
                    print('-----')
                    print('Du oppga HundeEierID',input_hunde_eier_id)
                    print('Denne eieren eksisterer ikke.')
                    print('-----')
                    
            # Hva som skjer hvis oppdretter ikke eksisterer   
            else:
                
                print('-----')
                print('Du oppga OppdretterIDen',input_oppdretter_id)
                print('Denne oppdretteren eksisterer ikke.')
                print('-----')

        svar = input('Vil du registrere en annen hund? ja/nei ')

        if svar == 'nei' or svar == 'n' or svar == 'Nei' or svar == 'NEI':
            fortsette = False
            print('Program avsluttet!')

registrer_ny_hund()






        


        

        

        
