import os

def slett_hundeeier():

    fortsette = True

    while fortsette == True:

        finnes = False

        input_hunde_eier_id = input('Oppgi HundeEierID på eieren som skal slettes: ')

        # Åpner hund.txt for å sjekke om eieren har en hund registrert. Leser første linje
        hund_fil = open('hund.txt', 'r')
        hunde_id = hund_fil.readline()

        while hunde_id != '':

            # Leser linje 2 til og med 6
            oppdretter_id = hund_fil.readline()
            hunde_eier_id = hund_fil.readline()
            hund_navn = hund_fil.readline()
            hund_kjonn = hund_fil.readline()
            hund_fodt = hund_fil.readline()

            # Fjerner linjeskift

            hunde_id = hunde_id.rstrip('\n')
            oppdretter_id = oppdretter_id.rstrip('\n')
            hunde_eier_id = hunde_eier_id.rstrip('\n')
            hund_navn = hund_navn.rstrip('\n')
            hund_kjonn = hund_kjonn.rstrip('\n')
            hund_fodt = hund_fodt.rstrip('\n')

            if input_hunde_eier_id == hunde_eier_id:

                finnes = True

            hunde_id = hund_fil.readline()

        # Hvis eieren har en hund registrert
        if finnes == True:
            hund_fil.close()
            
            print('-----')
            print('Du oppga HundeEierID',input_hunde_eier_id)
            print('Denne eieren har en hund registrert i systemet og kan derfor ikke slettes.')
            print('-----')

        # Hvis eieren ikke har en hund registrert
        else:
            hund_fil.close()

            hundeeier_fil = open('hundeeier.txt','r')
            temp_fil = open('temp.txt','w')

            hunde_eier_fil_id = hundeeier_fil.readline()

            while hunde_eier_fil_id != '':
                
                # Leser andre og tredje linje 
                hunde_eier_fil_fornavn = hundeeier_fil.readline()
                hunde_eier_fil_etternavn = hundeeier_fil.readline()

                # Fjerner linjeskift \n

                hunde_eier_fil_id = hunde_eier_fil_id.rstrip('\n')
                hunde_eier_fil_fornavn = hunde_eier_fil_fornavn.rstrip('\n')
                hunde_eier_fil_etternavn = hunde_eier_fil_etternavn.rstrip('\n')

                if input_hunde_eier_id != hunde_eier_fil_id:
                    temp_fil.write(hunde_eier_fil_id + '\n')
                    temp_fil.write(hunde_eier_fil_fornavn + '\n')
                    temp_fil.write(hunde_eier_fil_etternavn + '\n')

                hunde_eier_fil_id = hundeeier_fil.readline()

            hundeeier_fil.close()
            temp_fil.close()

            os.remove('hundeeier.txt')
            os.rename('temp.txt','hundeeier.txt')

            print('-----')
            print('Du oppga',input_hunde_eier_id)
            print('Denne eieren har blitt slettet.')
            print('-----')

        svar = input('Vil du slette en annen eier? ja/nei ')

        if svar == 'nei' or svar == 'n' or svar == 'NEI' or svar == 'Nei':
            fortsette = False
            print('Program avsluttet!')

                
slett_hundeeier()

            
            

            

            
            
                

            

            
