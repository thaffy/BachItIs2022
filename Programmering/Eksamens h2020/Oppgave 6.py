def hunder_fra_kennel():

    fortsette = True

    while fortsette == True:

        input_kennelnavn = input('Oppgi kennelnavn: ')

        funnet = False

        oppdretter_fil = open('oppdretter.txt','r')

        oppdretter_id = oppdretter_fil.readline()

        while oppdretter_id != '':
            
            kennelnavn = oppdretter_fil.readline()
            kenneleier_fornavn = oppdretter_fil.readline()
            kenneleier_etternavn = oppdretter_fil.readline()

            oppdretter_id = oppdretter_id.rstrip('\n')
            kennelnavn = kennelnavn.rstrip('\n')
            kenneleier_fornavn = kenneleier_fornavn.rstrip('\n')
            kenneleier_etternavn = kenneleier_etternavn.rstrip('\n')

            if input_kennelnavn == kennelnavn:
                funnet = True

                oppdretter_id_funnet = oppdretter_id

            oppdretter_id = oppdretter_fil.readline()

        if funnet == True:
            oppdretter_fil.close()
            
            hund_funnet = False
            hund_fil = open('hund.txt','r')



            hunde_id = hund_fil.readline()

            while hunde_id != '':
                hund_oppdretter_id = hund_fil.readline()
                hund_eier_id = hund_fil.readline()
                hund_navn = hund_fil.readline()
                hund_kjonn = hund_fil.readline()
                hund_fodt = hund_fil.readline()

                hunde_id = hunde_id.rstrip('\n')
                hund_oppdretter_id = hund_oppdretter_id.rstrip('\n')
                hund_eier_id = hund_eier_id.rstrip('\n')
                hund_navn = hund_navn.rstrip('\n')
                hund_kjonn = hund_kjonn.rstrip('\n')
                hund_fodt = hund_fodt.rstrip('\n')

                if oppdretter_id_funnet == hund_oppdretter_id:
                    hund_funnet = True
                    hundeierfil = open('hundeeier.txt','r')

                    eierid = hundeierfil.readline()
                    while eierid != '':
                        eierid = eierid.rstrip('\n')
                        eierfornavn = hundeierfil.readline().rstrip('\n')
                        eieretternavn = hundeierfil.readline().rstrip('\n')

                        if hund_eier_id == eierid:
                            print('-----')
                            print("Eier's fornavn:",eierfornavn)
                            print("Eier's etternavn:",eieretternavn)
                        eierid = hundeierfil.readline()
                        
                    
                    
                    print('HundeID: ',hunde_id)
                    print('OppdretterID: ',hund_oppdretter_id)
                    print('Navn: ',hund_navn)
                    print('EierID: ',hund_eier_id)
                    print('Kjønn: ',hund_kjonn)
                    print('Født: ',hund_fodt)

                hunde_id = hund_fil.readline()

            if funnet != True:
                hund_fil.close()
                print('Denne kennelen har ingen hunder lagret i systemet.')

            else:
                hund_fil.close()


                    

            

        else:
            oppdretter_fil.close()
            print('Kennel eksisterer ikke i systemet.')


        svar = input('Vil du kjøre programmet på nytt? ja/nei ')
        if svar == 'nei' or svar == 'n' or svar == 'N' or svar == 'NEI' or svar == 'Nei':
            fortsette = False
            print('Program avsluttet')
        


hunder_fra_kennel()

                
            
